from sys import argv
import string
import secrets
import os
import qrcode
from qrcode.image import svg

factory = svg.SvgPathImage

def password_generator(seed=1):
    def desired_length():
        length = int(secrets.choice( range(1000) ) * 3.14 / 27) % 21
        # print(length)
        return length if length > 7 else desired_length()

    password    = ""
    characters  = string.ascii_letters + string.digits
    length      = int(seed) if seed > 7 and seed < 21 else desired_length()

    print("password length: {}".format(length))
    while True:
        password = ''.join(secrets.choice(characters) for i in range(length) )
        # print(password)
        if(any(ch.islower() for ch in password) and
            any(ch.isupper() for ch in password) and
                sum( ch.isdigit() for ch in password) >= 3):
            break
    return password

if __name__ == "__main__":
    print("--------------NOTE---------\n WE GENERATE SECURE PASSWORDS! IN ORDER TO PROVIDE THIS FEATURE, NO PASSWORD CAN HAVE A LENGTH LESS THAN 8!\n\n")
    if len(argv) <= 2:
        if len(argv) == 1 or not argv[1].isnumeric() :
            print("Password generator will generate a password with a random length.")
            pswd = password_generator()
        else:
            print("Password generator will generate a password with the given length: {} if it is possible. Or, length will be randomly chosen.".format(argv[1]))
            pswd = password_generator( int(argv[1]) )
        print("Generated password is: {}".format(pswd))
    
    elif len(argv) == 3 or len(argv) == 4 or len(argv) == 5 or len(argv) == 6:
        username    = argv[3] if len(argv) > 3 else ""
        length      = argv[5] if len(argv) > 5 else "1"
        mode        = argv[4] if len(argv) > 4 else "t"

        if length.isnumeric():
            length = int(length)
            print("Password generator will generate a password with the given length: {}.".format(length))
        else:
            length = 1
            print("Provided length is not a number, length will be chosen randomly between 7 and 21.")
        
        password_f_path = argv[1]
        program_name    = argv[2]
        cwd             = os.getcwd()

        if password_f_path.count('/') == 0:
            password_f_path = cwd + "/" + password_f_path
        
        pswd = password_generator( length )
        password_data = "\nProgram Name: {}\nUsername: {}\nPassword: {}\n".format(program_name, username, pswd)

        # print("mode is: {}".format(mode))

        if mode.count('t') > 0:
            # print("Will be written to text.")
            with open(password_f_path,'a') as f:
                f.write(password_data)
                # print("Password is written to file: {}".format(password_f_path))
        
        if mode.count('i') > 0:
            # print("Will be written to image.")
            img_path_list   = password_f_path.split('/')
            f_name          = img_path_list[-1].strip('.~/').split('.')[0]
            img_path = '/' + '/'.join(img_path_list[: len(img_path_list)-1 ]) + '/' + program_name + '.png'
            
            # print(img_path)
            img = qrcode.make(password_data, image_factory=factory)
            img.save(img_path)

    else:
        print("Wrong number of parameters provided, program will be terminated!!!\n\n")
        # print("This program can be run with at most 4" +
        #  " parameters. Other options are not permitted.\n" +
        #  "-Without parameter: Random length password will be generated.\n" +
        #  "-With 1 parameter 'length': 'length' will be the length of the password " + 
        #  "if it is between 7 and 21.\n    Otherwise password will have a random length.\n" +
        #  "-With 2 parameters 'file_name', 'program_name' : Password will be generated at " +
        #  "a random length and the \n    generated password will be stored in the 'file_name'" +
        #  "under the line that is written \''program_name':\'.\n" +
        #  "--With 3 parameters 'file_name', 'program_name', 'length' : Password " +
        #  "will be generated at the given 'length' and the\n    generated password " +
        #  "will be stored in the 'file_name' " + "under the line that is written " + 
        #  "\n    \''program_name':\'" + "\n    Username: 'username'.\n" +
        #  "--With 4 parameters 'file_name', 'program_name', 'length', 'username' : Password " +
        #  "will be generated at the given 'length' and the\n    generated password " +
        #  "will be stored in the 'file_name' " + "under the line that is written " + 
        #  "\n    \''program_name':\'" + "\n    Username: 'username'.\n\n\n\n"
        #  + "Program will be terminated.")