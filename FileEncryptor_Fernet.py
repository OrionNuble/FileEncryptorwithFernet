import os
import sys
import random
from cryptography.fernet import Fernet

def GetFileExtension(FileName):

    NameParsed = FileName.split(".")

    return NameParsed[-1]

def DoesArrayContains(Array, Contains):

    for i in Array:

        if i == Contains:

            return True

    return False

def ArrayToString_OrViceVersa(Array = [], String = ""):

    ReturnArray = []
    ReturnString = ""

    if Array != [] and String == "":

        for i in Array:

            ReturnString += i

            if i != Array[-1]:

                ReturnString += ","

        return ReturnString

    elif Array == [] and String != "":

        ReturnArray = String.split(",")

        return ReturnArray

    else:

        return "ERR"

class Cryptograph():

    def __init__(self) -> None:

        self.Action = ""
        self.File_PATH = ""
        self.KeyFile_PATH = ""
        self.EncDecDir = ""
        self.SavedDirectory = ""
        self.SavedDataFile_PATH = r"C:\Users\tomok\OneDrive\Belgeler\FileEncSaveData.txt"

        self.InMemoryKeyFile = ""

        self.FileData = ""
        self.Key = ""

        self.NonOperatableFileExtensions = ["exe", "py", "key"]

    def Init(self):

        TempSavedDir = ""
        TempSavedDataSplitted = []

        TempSavedKeyFile = ""
        TempSavedDataSplitted = []

        if os.path.isfile(self.File_PATH):

            with open(self.File_PATH, "rb") as OpFile:

                self.FileData = OpFile.read()
                OpFile.close()

        if os.path.isfile(self.KeyFile_PATH):

            with open(self.KeyFile_PATH, "rb") as KeyFile:

                self.Key = KeyFile.read()
                KeyFile.close()

        if os.path.isfile(self.SavedDataFile_PATH):

            with open(self.SavedDataFile_PATH, "r") as RememberDirectoryFile:

                TempSavedDir = RememberDirectoryFile.read()
                RememberDirectoryFile.close()

            TempSavedDataSplitted = TempSavedDir.split(";")

            self.SavedDirectory = TempSavedDataSplitted[0]

            self.InMemoryKeyFile = TempSavedDataSplitted[1]

            self.NonOperatableFileExtensions = ArrayToString_OrViceVersa([], TempSavedDataSplitted[2])

        return self.FileData, self.Key

    def SaveData(self, Data, Type):

        OrgData = ""
        Splitted = [" ", " ", " "]
        NewData = ""

        ArrayStringData = ""

        if os.path.isfile(self.SavedDataFile_PATH):

            with open(self.SavedDataFile_PATH, "r") as RD_P:

                OrgData = RD_P.read()
                RD_P.close()

            Splitted = OrgData.split(";")

            if Type == "Dir":

                Splitted[0] = Data

            elif Type == "KeyFile":

                Splitted[1] = Data

            elif Type == "NonOperable":

                ArrayStringData = ArrayToString_OrViceVersa(self.NonOperatableFileExtensions)

                Splitted[2] = ArrayStringData

            else:

                print(cryptograph.DisplayError("WRONG_SAVE_TYPE: COULD NOT BE SAVED", Type))

                return True, False


        else:

            if Type == "Dir":

                Splitted[0] = Data

            elif Type == "KeyFile":

                Splitted[1] = Data

            elif Type == "NonOperable":

                ArrayStringData = ArrayToString_OrViceVersa(self.NonOperatableFileExtensions)

                Splitted[2] = ArrayStringData

            else:

                print(cryptograph.DisplayError("WRONG_SAVE_TYPE: COULD NOT BE SAVED", Type))

                return True, False


        NewData += Splitted[0] + ";" + Splitted[1] + ";" + Splitted[2]

        with open(self.SavedDataFile_PATH, "w") as RD_P_W:

            RD_P_W.write(NewData)
            RD_P_W.close()

    def FileCheck(self, FileToCheck):

        if os.path.isfile(FileToCheck):

            return True

        return False

    def GenerateKey(self, KeyFileName, Mode):

        GeneratedKey = ""

        GeneratedKey = Fernet.generate_key()

        NewKeyFileName = ""

        if Mode == "Deviate":

            NewKeyFileName = KeyFileName + "_" + str(random.randint(0, 1000))

        else:

            NewKeyFileName = KeyFileName

        with open(NewKeyFileName + ".key", "wb") as KeyFile:

            KeyFile.write(GeneratedKey)
            KeyFile.close()

        return NewKeyFileName + ".key"

    def DisplayError(self, Err, Variable):

        if Err == "NO COMMAND":

            return "\ncommand error: no command given\n"

        elif Err == "NO COMMAND BODY":

            return "\ncommand error: no body given: " + Variable + "\n"

        elif Err == "MISSING COMMAND BODY":

            return "\ncommand error: command body is missing: " + Variable + "\n"

        elif Err == "COMMAND NOT RECOGNIZED":

            return "\ncommand error: command: " + Variable + " not recognized\n"

        elif Err == "SYNTAX ERROR: ERROR":

            return "\nsyntax error: syntax: " + Variable + " not recognized\n"

        elif Err == "NO DIRECTORY GIVEN":

            return "\ndirectory error: no directory given\n"

        elif Err == "NO PATH GIVEN":

            return "\npath error: no path given\n"

        elif Err == "DIRECTORY NOT FOUND: DIR":

            return "\ndirectory error: directory not found: " + Variable + "\n"

        elif Err == "PATH NOT FOUND: PATH":

            return "\npath error: path not found: " + Variable + "\n"

        elif Err == "NO KEY FILE IN MEMORY":

            return "\nmemory error: no key file found\n"

        elif Err == "KEY NOT FOUND":

            return "\nkey error: no key found\n"

        elif Err == "CANNOT USE FRESH KEY FOR DECRYPTION":

            return "\nkey error: must use an already existing key for decryption\n"

        elif Err == "NO INPUT FOR PRINT":

            return "\ndisplay error: no input for the [print] command\n"

        elif Err == "INVALID SYNTAX: SYNTAX":

            return "\nsyntax error: invalid syntax: given command does not match with this syntax: " + Variable + "\n"

        elif Err == "MISSING ENCRYPTION DATA":

            return "\nencryption error: required data is missing\n"

        elif Err == "MISSING DECRYPTION DATA":

            return "\ndecryption error: required data is missing\n"
        
        elif Err == "CANNOT OPERATE ON NON OPERATABLE FILE TYPES: FILE EXTENSION":

            return "\nfile error: file has non-operable extension: extension: *." + Variable + "\n"

        else:

            return "\nunknown error\n"

    def DisplayWarning(self, Warn, Variable):

        if Warn == "FILE ALREADY EXISTS":

            print("\nWARNING: Given file already exists. file: " + Variable + ". If you proceed, the file will be overwritten. type: y to continue, n to cancel.\n")

        elif Warn == "WARNING: EXTENSION DOES NOT EXIST, SO IT COULD NOT BE REMOVED":

            print("\nWARNING: Given file extension was not a non-operable, so it could not be removed. File extension: *." + Variable + "\n")

        else:

            return "unknown warning"

    def RemoveDirPrefix(self, String):

        Removed = ""

        for i in range(len(String)):

            if i != 0 and i != 1 and i != 2 and i != 3:

                Removed += String[i]

        return Removed

    def EncryptMultiple(self):

        self.EncDecDir = self.File_PATH

        for File in os.listdir(self.EncDecDir):

            if not DoesArrayContains(self.NonOperatableFileExtensions, GetFileExtension(File)):

                self.File_PATH = self.EncDecDir + "\\" + File

                self.Init()

                self.Encrypt()

            else:

                print(self.DisplayError("CANNOT OPERATE ON NON OPERATABLE FILE TYPES: FILE EXTENSION", GetFileExtension(File)))

    def DecryptMultiple(self):

        self.EncDecDir = self.File_PATH

        for File in os.listdir(self.EncDecDir):

            if not DoesArrayContains(self.NonOperatableFileExtensions, GetFileExtension(File)):

                self.File_PATH = self.EncDecDir + "\\" + File

                self.Init()

                self.Decrypt()

            else:

                print(self.DisplayError("CANNOT OPERATE ON NON OPERATABLE FILE TYPES: FILE EXTENSION", GetFileExtension(File)))

    def Encrypt(self):

        if self.Key == "" or self.FileData == "":

            print(self.DisplayError("MISSING ENCRYPTION DATA", ""))

            return

        encryptedFileContents = Fernet(self.Key).encrypt(self.FileData)

        with open(self.File_PATH, "wb") as EncFile:

            EncFile.write(encryptedFileContents)
            EncFile.close()

    def Decrypt(self):

        if self.Key == "" or self.FileData == "":

            print(self.DisplayError("MISSING DECRYPTION DATA", ""))

            return

        decryptedFileContents = Fernet(self.Key).decrypt(self.FileData)

        with open(self.File_PATH, "wb") as DecFile:
            DecFile.write(decryptedFileContents)
            DecFile.close()

cryptograph = Cryptograph()

def isIndexValid(Array, Index):
    if Index >= 0 and Index < len(Array):
        return True

    return False

def contains_str(String, LookFor, startInd):

    if len(LookFor) + startInd <= len(String):

        for i in range(len(LookFor)):

            if String[i + startInd] != LookFor[i]:

                return False

        return True

    else:

        return False

def TerminalInputParser(Input):

    InputSplitted = []

    ACCEPTED_COMMANDS = ["encrypt", "decrypt", "generate_key", "cd", "pwd", "sd", "non_operables", "print", "ls", "clear", "--help", "exit"]

    PARSED_TERMINAL_INPUT = []

    InputSplitted = Input.split(" ")

    COMMAND = ""

    IDENTIFIER_ONE = ""

    FILE_ONE = ""

    IDENTIFIER_TWO = ""

    FILE_TWO = ""

    SecondIdentifierReached = False

    if len(InputSplitted) != 0:

        if DoesArrayContains(ACCEPTED_COMMANDS, InputSplitted[0]):

            if InputSplitted[0] == "encrypt" or InputSplitted[0] == "decrypt":

                for i in range(len(InputSplitted)):

                    if i == 0:

                        COMMAND = InputSplitted[0]

                    elif i == 1:

                        IDENTIFIER_ONE = InputSplitted[1]

                    elif i == 2:

                        FILE_ONE += InputSplitted[2]

                    elif i >= 3:

                        if InputSplitted[i] != "-w" and InputSplitted[i] != "--fresh" and InputSplitted[i] != "dir.fresh" and not SecondIdentifierReached:

                            FILE_ONE += " "
                            FILE_ONE += InputSplitted[i]

                        elif InputSplitted[i] == "-w" or InputSplitted[i] == "--fresh" or InputSplitted[i] == "dir.fresh":

                            IDENTIFIER_TWO = InputSplitted[i]

                            SecondIdentifierReached = True

                        else:

                            FILE_TWO += InputSplitted[i]
                            FILE_TWO += " "

                FILE_TWO = FILE_TWO[:-1]

            elif InputSplitted[0] == "generate_key":

                for i in range(len(InputSplitted)):

                    if i == 0:

                        COMMAND = InputSplitted[0]

                    elif i == 1:

                        IDENTIFIER_ONE = InputSplitted[1]

                    elif i >= 2:

                        FILE_ONE += InputSplitted[i]
                        FILE_ONE += " "

                FILE_ONE = FILE_ONE[:-1]

            elif InputSplitted[0] == "cd" or InputSplitted[0] == "sd" or InputSplitted[0] == "print" or InputSplitted[0] == "--help":

                for i in range(len(InputSplitted)):

                    if i == 0:

                        COMMAND = InputSplitted[0]

                    elif i >= 1:

                        FILE_ONE += InputSplitted[i]
                        FILE_ONE += " "

                FILE_ONE = FILE_ONE[:-1]

            elif InputSplitted[0] == "non_operables":

                COMMAND = InputSplitted[0]

                for i in range(len(InputSplitted)):

                    if i == 1:

                        IDENTIFIER_ONE = InputSplitted[1]

                    elif i >= 2:

                        FILE_ONE += InputSplitted[i]

            elif InputSplitted[0] == "ls" or InputSplitted[0] == "pwd" or InputSplitted[0] == "clear" or InputSplitted[0] == "exit":

                COMMAND = InputSplitted[0]

        else:

            if len(InputSplitted[0]) == 0:

                COMMAND = "NONE"

            else:

                COMMAND = InputSplitted[0]


    PARSED_TERMINAL_INPUT.append(COMMAND)
    PARSED_TERMINAL_INPUT.append(IDENTIFIER_ONE)
    PARSED_TERMINAL_INPUT.append(FILE_ONE)
    PARSED_TERMINAL_INPUT.append(IDENTIFIER_TWO)
    PARSED_TERMINAL_INPUT.append(FILE_TWO)

    return PARSED_TERMINAL_INPUT

def TerminalInputCommenter(ParsedInput):

    COMMENTED_INPUT = []

    ACCEPTED_COMMANDS = ["encrypt", "decrypt", "generate_key", "non_operables", "cd", "pwd", "sd", "print", "ls", "clear", "--help", "exit"]
    ACCEPTED_FIRST_IDENTIFIERS = ["-i", "-dir", "-o"]
    ACCEPTED_SECOND_IDENTIFIERS = ["-w", "--fresh", "dir.fresh"]

    Command = ParsedInput[0]
    Id_One = ParsedInput[1]
    File_One = ParsedInput[2]
    Id_Two = ParsedInput[3]
    File_Two = ParsedInput[4]

    if ParsedInput[0] == "NONE":

        print(cryptograph.DisplayError("NO COMMAND", ParsedInput[0]))

        return [], False

    if Command == "encrypt" or Command == "decrypt":

        if not DoesArrayContains(ACCEPTED_FIRST_IDENTIFIERS, Id_One):

            if Id_One == "":

                print(cryptograph.DisplayError("NO COMMAND BODY", Command))

            else:

                print(cryptograph.DisplayError("SYNTAX ERROR: ERROR", Id_One))

            return [], False

        else:

            if contains_str(File_One, "dir.", 0):

                File_One = cryptograph.SavedDirectory + "\\" + cryptograph.RemoveDirPrefix(File_One)

            elif File_One == "local":

                File_One = os.getcwd()

            if Id_One == "-i":

                if not os.path.isfile(File_One):

                    if File_One == "":

                        print(cryptograph.DisplayError("NO PATH GIVEN", ""))

                    else:

                        print(cryptograph.DisplayError("PATH NOT FOUND: PATH", File_One))

                    return [], False

            elif Id_One == "-dir":

                if not os.path.isdir(File_One):

                    if File_One == "":

                        print(cryptograph.DisplayError("NO DIRECTORY GIVEN", ""))

                    else:

                        print(cryptograph.DisplayError("DIRECTORY NOT FOUND: DIR", File_One))

                        return [], False

                else:

                    Command += "_m"

            elif Id_One == "-o":

                print(cryptograph.DisplayError("INVALID SYNTAX: SYNTAX", Id_One))

                return [], False

            if not DoesArrayContains(ACCEPTED_SECOND_IDENTIFIERS, Id_Two):

                    if Id_Two == "":

                        print(cryptograph.DisplayError("MISSING COMMAND BODY", Command))

                    else:

                        print(cryptograph.DisplayError("SYNTAX ERROR: ERROR", Id_Two))

                    return [], False

            else:

                    if Id_Two == "-w":

                        if contains_str(File_Two, "dir.", 0):

                            File_Two = cryptograph.SavedDirectory + "\\" + cryptograph.RemoveDirPrefix(File_Two)

                        if not os.path.isfile(File_Two):

                            print(cryptograph.DisplayError("PATH NOT FOUND: PATH", File_Two))

                            return [], False
             
                    elif Id_Two == "--fresh":

                        if Command != "decrypt":

                            File_Two = cryptograph.GenerateKey("FreshEncKey", "Deviate")

                            cryptograph.InMemoryKeyFile = File_Two

                            cryptograph.SaveData(cryptograph.InMemoryKeyFile, "KeyFile")

                        else:

                            print(cryptograph.DisplayError("CANNOT USE FRESH KEY FOR DECRYPTION", ""))

                            return [], False

                    elif Id_Two == "dir.fresh":

                        if Command != "decrypt":

                            File_Two = cryptograph.GenerateKey(cryptograph.SavedDirectory + "\\FreshEncKey", "Deviate")
                            
                            cryptograph.InMemoryKeyFile = File_Two

                            cryptograph.SaveData(cryptograph.InMemoryKeyFile, "KeyFile")

                        else:

                            print(cryptograph.DisplayError("CANNOT USE FRESH KEY FOR DECRYPTION", ""))

                            return [], False

    elif Command == "generate_key":

        if Id_One != "-o":

            if Id_One == "":

                print(cryptograph.DisplayError("MISSING COMMAND BODY", Command))

                return [], False

            elif not DoesArrayContains(ACCEPTED_FIRST_IDENTIFIERS, Id_One):

                print(cryptograph.DisplayError("SYNTAX ERROR: ERROR", Id_One))

                return [], False

            else:

                print(cryptograph.DisplayError("INVALID SYNTAX: SYNTAX", Id_One))

        else:

            if contains_str(File_One, "dir.", 0):

                File_One = cryptograph.SavedDirectory + "\\" + cryptograph.RemoveDirPrefix(File_One)

            if os.path.isfile(File_One + ".key"):

                cryptograph.DisplayWarning("FILE ALREADY EXISTS", File_One + ".key ")
                contorcancel = input("> ")

                if contorcancel != "y" and contorcancel != "Y":

                    print("command canceled")

                    return [], False

    elif Command == "sd" or Command == "cd" or Command == "print" or Command == "--help":

        if Command == "sd" or Command == "cd":

            if not os.path.isdir(File_One):

                print(cryptograph.DisplayError("DIRECTORY NOT FOUND: DIR", File_One))

                return [], False

        elif Command == "print":

            if File_One == "SavedKey_File":

                File_Two = cryptograph.InMemoryKeyFile

            elif File_One == "SavedKey_Data":

                if os.path.isfile(cryptograph.InMemoryKeyFile):

                    with open(cryptograph.InMemoryKeyFile, "rb") as KF:

                        File_Two = KF.read()
                        KF.close()

                else:

                    File_Two = "empty"

            elif File_One == "SavedDirectory":

                File_Two = cryptograph.SavedDirectory

            elif File_One == "NonOperables":

                print(cryptograph.NonOperatableFileExtensions)

            else:

                File_Two = File_One

    elif Command == "non_operables":

        if Id_One == "-add":

            AdditionsSplitted = File_One.split(",")

            for i in AdditionsSplitted:

                if len(i) != 0:

                    if i[-1] == ",":

                        i = i[:-1]

            for i in AdditionsSplitted:

                if len(i) != 0:

                    cryptograph.NonOperatableFileExtensions.append(i)

                    cryptograph.SaveData(cryptograph.NonOperatableFileExtensions, "NonOperable")

        elif Id_One == "-remove":

            RemovalsSplitted = File_One.split(",")

            for i in RemovalsSplitted:

                if len(i) != 0:

                    if i[-1] == ",":

                        i = i[:-1]

            for i in RemovalsSplitted:

                if DoesArrayContains(cryptograph.NonOperatableFileExtensions, i):

                    if len(i) != 0:

                        cryptograph.NonOperatableFileExtensions.remove(i)

                        cryptograph.SaveData(cryptograph.NonOperatableFileExtensions, "NonOperable")

                else:

                    cryptograph.DisplayWarning("WARNING: EXTENSION DOES NOT EXIST, SO IT COULD NOT BE REMOVED", i)

        else:

            if not DoesArrayContains(ACCEPTED_FIRST_IDENTIFIERS, Id_One):

                print(cryptograph.DisplayError("SYNTAX ERROR: ERROR", Id_One))

            else:

                print(cryptograph.DisplayError("INVALID SYNTAX: SYNTAX", Id_One))

    elif Command != "ls" and Command != "pwd" and Command != "clear" and Command != "exit":

        print(cryptograph.DisplayError("COMMAND NOT RECOGNIZED", Command))

    COMMENTED_INPUT.append(Command)
    COMMENTED_INPUT.append(Id_One)
    COMMENTED_INPUT.append(File_One)
    COMMENTED_INPUT.append(Id_Two)
    COMMENTED_INPUT.append(File_Two)

    return COMMENTED_INPUT, True

def Terminal(Input):

    cryptograph.Init()

    terminal_input = input("FernetFileEncrpytor-Decryptor@root#: ")

    #terminal_input = Input

    ParsedTerminalInput = TerminalInputParser(terminal_input)

    CommentedTerminalInput, Status = TerminalInputCommenter(ParsedTerminalInput)

    if not Status:

        return True, False

    COMMAND = CommentedTerminalInput[0]
    FILE_ONE = CommentedTerminalInput[2]
    FILE_TWO = CommentedTerminalInput[4]

    if CommentedTerminalInput[0] == "encrypt" or CommentedTerminalInput[0] == "decrypt" or CommentedTerminalInput[0] == "encrypt_m" or CommentedTerminalInput[0] == "decrypt_m":

        cryptograph.Action = COMMAND
        cryptograph.File_PATH = FILE_ONE
        cryptograph.KeyFile_PATH = FILE_TWO
        cryptograph.InMemoryKeyFile = cryptograph.KeyFile_PATH

        return True, True

    elif CommentedTerminalInput[0] == "generate_key":

        generatedkeyfile = cryptograph.GenerateKey(FILE_ONE, "DontDeviate")

        cryptograph.InMemoryKeyFile = generatedkeyfile

        cryptograph.SaveData(cryptograph.InMemoryKeyFile, "KeyFile")

    elif CommentedTerminalInput[0] == "cd" or CommentedTerminalInput[0] == "sd" or CommentedTerminalInput[0] == "print" or CommentedTerminalInput[0] == "--help":

        if CommentedTerminalInput[0] == "cd":

            os.chdir(FILE_ONE)

        elif CommentedTerminalInput[0] == "sd":

            cryptograph.SavedDirectory = FILE_ONE

            cryptograph.SaveData(cryptograph.SavedDirectory, "Dir")

        elif CommentedTerminalInput[0] == "print":

            print(str(FILE_TWO) + "\n")

        elif CommentedTerminalInput[0] == "--help":

            print("\nFernet File Encryptor/Decryptor. Usage:\n")
            print("        -param1 -> Command\n\n")
            print("        -param2 -> File Identifier\n\n")
            print("        -param3 -> File to Operate on\n\n")
            print("        -param4 -> Key File Identifier\n\n")
            print("        -param5 -> Key File\n\n")

            print("Allowed params:\n")
            print("        -param1 - allowed commands: encrypt, decrypt, generate_key, non_operables, cd, pwd, sd, print, ls, clear, --help, exit")
            print("        -param2 - allowed file identifiers: -i, -dir, -o")
            print("        -param3 - allowed key file identifiers: -w, dir.fresh, --fresh")
            print("        -additional keywords: dir.\n\n")

            print("        command: encrypt: Description:   Command for encrypting a file\n")
            print("        command: decrypt: Description:   Command for decrypting a file\n")
            print("        command: generate_key: Description:   Used for key generation. Can be supplied with a name and path, or will generate a key with a fixed name and the path will be the cwd\n")
            print("        command: non_operables: Description:   Supply with an option (--add or --remove) to add or remove file extensions that cannot be operated on\n")
            print("        command: cd: Description:   If supplied with a valid directory, will change the cwd to the supplied directory\n")
            print("        command: pwd: Description:   Will print the current cwd\n")
            print("        command: sd: Description:   If supplied with a valid directory, will save the directory to a file. Then, the saved directory can be used with the keyword 'dir.'\n")
            print("        command: print: Description:   If supplied with valid arguments, will print the requested data. If not, it will print whatever string was inputted\n")
            print("        command: ls: Description:   Will print all the files and folders in the cwd. Same thing as ls in linux and dir in windows\n")
            print("        command: clear: Description:   Will clear the console\n")
            print("        command: --help: Description:   Will display this message\n")
            print("        command: exit: Description:   Will exit the application\n\n")

            print("        identifier: -i: Description:   Identifiers the beginning of file input. Stands for 'input'. It means that the operation is going to be done on a single file\n")
            print("        identifier: -dir: Description:   Identifies the beginning of a dir input. Stands for 'directory'. It means that the operation is going to be done on an entire directory\n")
            print("        identifier: -o: Description:   Identifies the beginning of a output name. Stands for 'output'\n")
            print("        identifier: -w: Description:   Identifies the end of a file input and beginning of a key file input. Stands for 'with'\n")
            print("        identifier: dir.fresh: Description:   If used, will generate a brand new (fresh) key, in the directory that was saved using 'sd'\n")
            print("        identifier: --fresh: Description:   If used, will generate a brand new (fresh) key, in the local (cwd) directory\n")
            print("        keyword: dir.: Description:   Will be replaced with the saved directory\n")

    elif CommentedTerminalInput[0] == "ls" or CommentedTerminalInput[0] == "pwd" or CommentedTerminalInput[0] == "clear" or CommentedTerminalInput[0] == "exit":

        if CommentedTerminalInput[0] == "ls":

            FilesList = os.listdir(os.getcwd())

            FilesStr = ""

            for i in range(len(FilesList)):

                if i != 0:

                    FilesStr += "   "

                else:

                    FilesStr += "  "

                FilesStr += FilesList[i]

            print(FilesStr)

        elif CommentedTerminalInput[0] == "pwd":

            print(os.getcwd() + "\n")

        elif CommentedTerminalInput[0] == "clear":

            os.system("cls")

        elif CommentedTerminalInput[0] == "exit":

            return False, False

    return True, False

run_terminal = True
Operate = False

while run_terminal:

    run_terminal, Operate = Terminal("")

    if Operate:

        cryptograph.Init()

        if cryptograph.Action == "encrypt":

            cryptograph.Encrypt()

        elif cryptograph.Action == "decrypt":

            cryptograph.Decrypt()

        elif cryptograph.Action == "encrypt_m":

            cryptograph.EncryptMultiple()

        elif cryptograph.Action == "decrypt_m":

            cryptograph.DecryptMultiple()
