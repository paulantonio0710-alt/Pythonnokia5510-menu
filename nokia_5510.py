

def phone_book():
        print("""
===== PHONE BOOK =====
1. Search
2. Service Nos.
3. Add name
4. Erase
5. Edit
6. Copy
7. Assign tone
8. Send b'card
9. Options
10. Speed dials
11. Voice tags
0. Back
""")
        choice = input("Choose an option: ")
        match choice:
            case "1":
                print("Search selected.")
                phone_book()
            case "2":
                print("Service Nos. selected.")
                phone_book()
            case "3":
                print("Add name selected.")
                phone_book()
            case "4":
                print("Erase selected.")
                phone_book()
            case "5":
                print("Edit selected.")
                phone_book()
            case "6":
                print("Copy selected.")
                phone_book()
            case "7":
                print("Assign tone selected.")
                phone_book()
            case "8":
                print("Send b'card selected.")
                phone_book()
            case "9":
                phone_options()
            case "10":
                print("Speed dials selected.")
                phone_book()
            case "11":
                print("Voice tags selected.")
                phone_book()
            case "0":
                main_menu()
            case _:
                print("Invalid option.")
                phone_book()
                


def phone_options():
        print("""
===== OPTIONS =====
1. Memory in use
2. Type of view
3. Memory status
0. Back
""")
        choice = input("Choose an option: ")
        match choice:
            case "1":
                print("Memory in use selected.")
                phone_options()
            case "2":
                print("Type of view selected.")
                phone_options()
            case "3":
                print("Memory status selected.")
                phone_options()
            case "0":
                phone_book()
            case _:
                print("Invalid option, try again.")
                phone_options()


def messages():
        print("""
===== MESSAGES =====
1. Write messages
2. Inbox
3. Outbox
4. Picture messages
5. Templates
6. Smileys
7. Message settings
8. Info service
9. Voice mailbox number
10. Service command editor
0. Back
""")
        choice = input("Choose an option: ")
        match choice:
            case "1":
                print("Write messages selected.")
                messages()
            case "2":
                print("Inbox selected.")
                messages()
            case "3":
                print("Outbox selected.")
                messages()
            case "4":
                print("Picture messages selected.")
                messages()
            case "5":
                print("Templates selected.")
                messages()
            case "6":
                print("Smileys selected.")
                messages()
            case "7":
                message_settings()
            case "8":
                print("Info service selected.")
                messages()
            case "9":
                print("Voice mailbox number selected.")
                messages()
            case "10":
                print("Service command editor selected.")
                messages()
            case "0":
                main_menu()
            case _:
                print("Invalid option, try again.")
                messages()


def message_settings():
        print("""
===== MESSAGE SETTINGS =====
1. Set 1
2. Common
0. Back
""")
        choice = input("Choose an option: ")
        match choice:
            case "1":
                message_set1()
            case "2":
                message_common()
            case "0":
                messages()
            case _:
                print("Invalid option, try again.")
                message_settings()


def message_set1():
        print("""
===== SET 1 =====
1. Message centre number
2. Messages sent as
3. Message validity
0. Back
""")
        choice = input("Choose an option: ")
        match choice:
            case "1":
                print("Message centre number selected.")
                message_set1()
            case "2":
                print("Messages sent as selected.")
                message_set1()
            case "3":
                print("Message validity selected.")
                message_set1()
            case "0":
                message_settings()
            case _:
                print("Invalid option, try again.")
                message_set1()


def message_common():
        print("""
===== COMMON =====
1. Delivery reports
2. Reply via same centre
3. Character support
0. Back
""")
        choice = input("Choose an option: ")
        match choice:
            case "1":
                print("Delivery reports selected.")
                message_common()
            case "2":
                print("Reply via same centre selected.")
                message_common()
            case "3":
                print("Character support selected.")
                message_common()
            case "0":
                message_settings()
            case _:
                print("Invalid option, try again.")
                message_common()


def call_register():
        print("""
===== CALL REGISTER =====
1. Missed calls
2. Received calls
3. Dialled numbers
4. Erase recent call lists
5. Show call duration
6. Show call costs
7. Call cost settings
8. Prepaid credit
0. Back
""")
        choice = input("Choose an option: ")
        match choice:
            case "1":
                print("Missed calls selected.")
                call_register()
            case "2":
                print("Received calls selected.")
                call_register()
            case "3":
                print("Dialled numbers selected.")
                call_register()
            case "4":
                print("Erase recent call lists selected.")
                call_register()
            case "5":
                call_duration()
            case "6":
                call_costs()
            case "7":
                call_cost_settings()
            case "8":
                print("Prepaid credit selected.")
                call_register()
            case "0":
                main_menu()
            case _:
                print("Invalid option, try again.")
                call_register()


def call_duration():
        print("""
===== SHOW CALL DURATION =====
1. Last call duration
2. All calls' duration
3. Received calls' duration
4. Dialled calls' duration
5. Clear timers
0. Back
""")
        choice = input("Choose an option: ")
        match choice:
            case "1":
                print("Last call duration selected.")
                call_duration()
            case "2":
                print("All calls' duration selected.")
                call_duration()
            case "3":
                print("Received calls' duration selected.")
                call_duration()
            case "4":
                print("Dialled calls' duration selected.")
                call_duration()
            case "5":
                print("Clear timers selected.")
                call_duration()
            case "0":
                call_register()
            case _:
                print("Invalid option, try again.")
                call_duration()


def call_costs():
        print("""
===== SHOW CALL COSTS =====
1. Last call cost
2. All calls' cost
3. Clear counters
0. Back
""")
        choice = input("Choose an option: ")
        match choice:
            case "1":
                print("Last call cost selected.")
                call_costs()
            case "2":
                print("All calls' cost selected.")
                call_costs()
            case "3":
                print("Clear counters selected.")
                call_costs()
            case "0":
                call_register()
            case _:
                print("Invalid option, try again.")
                call_costs()


def call_cost_settings():
        print("""
===== CALL COST SETTINGS =====
1. Call cost limit
2. Show costs in
0. Back
""")
        choice = input("Choose an option: ")
        match choice:
            case "1":
                print("Call cost limit selected.")
                call_cost_settings()
            case "2":
                print("Show costs in selected.")
                call_cost_settings()
            case "0":
                call_register()
            case _:
                print("Invalid option, try again.")
                call_cost_settings()


def tones():
        print("""
===== TONES =====
1. Ringing tone
2. Ringing volume
3. Incoming call alert
4. Message alert tone
5. Keypad tones
6. Warning tones
7. Vibrating alert
8. Screen saver
0. Back
""")
        choice = input("Choose an option: ")
        match choice:
            case "1":
                print("Ringing tone selected.")
                tones()
            case "2":
                print("Ringing volume selected.")
                tones()
            case "3":
                print("Incoming call alert selected.")
                tones()
            case "4":
                print("Message alert tone selected.")
                tones()
            case "5":
                print("Keypad tones selected.")
                tones()
            case "6":
                print("Warning tones selected.")
                tones()
            case "7":
                print("Vibrating alert selected.")
                tones()
            case "8":
                print("Screen saver selected.")
                tones()
            case "0":
                main_menu()
            case _:
                print("Invalid option, try again.")
                tones()


def settings():
        print("""
===== SETTINGS =====
1. Call settings
2. Phone settings
3. Security settings
4. Restore factory settings
0. Back
""")
        choice = input("Choose an option: ")
        match choice:
            case "1":
                call_settings()
            case "2":
                phone_settings()
            case "3":
                security_settings()
            case "4":
                print("Restore factory settings selected.")
            case "0":
                main_menu()
            case _:
                print("Invalid option, try again.")
                settings()


def call_settings():
        print("""
===== CALL SETTINGS =====
1. Automatic redial
2. Speed dialling
3. Call waiting options
4. Own number sending
5. Phone line in use
6. Automatic answer
0. Back
""")
        choice = input("Choose an option: ")
        match choice:
            case "1":
                print("Automatic redial selected.")
                call_settings() 
            case "2":
                print("Speed dialling selected.")
                call_settings()
            case "3":
                print("Call waiting options selected.")
                call_settings()
            case "4":
                print("Own number sending selected.")
                call_settings()
            case "5":
                print("Phone line in use selected.")
                call_settings()
            case "6":
                print("Automatic answer selected.")
                call_settings()
            case "0":
                settings()
            case _:
                print("Invalid option, try again.")
                call_settings()


def phone_settings():
        print("""
===== PHONE SETTINGS =====
1. Language
2. Cell info display
3. Welcome note
4. Network selection
5. Confirm SIM service actions
0. Back
""")
        choice = input("Choose an option: ")
        match choice:
            case "1":
                print("Language selected.")
                phone_settings()
            case "2":
                print("Cell info display selected.")
                phone_settings()
            case "3":
                print("Welcome note selected.")
                phone_settings()
            case "4":
                print("Network selection selected.")
                phone_settings()
            case "5":
                print("Confirm SIM service actions selected.")
                phone_settings()
            case "0":
                settings()
            case _:
                print("Invalid option, try again.")
                phone_settings()


def security_settings():
        print("""
===== SECURITY SETTINGS =====
1. PIN code request
2. Call barring service
3. Fixed dialling
4. Closed user group
5. Security level
6. Change access codes
0. Back
""")
        choice = input("Choose an option: ")
        match choice:
            case "1":
                print("PIN code request selected.")
                security_settings()
            case "2":
                print("Call barring service selected.")
                security_settings()
            case "3":
                print("Fixed dialling selected.")
                security_settings()
            case "4":
                print("Closed user group selected.")
                security_settings()
            case "5":
                print("Security level selected.")
                security_settings()
            case "6":
                print("Change access codes selected.")
                security_settings()
            case "0":
                settings()
            case _:
                print("Invalid option, try again.")
                security_settings()


def music():
        print("""
===== MUSIC =====
1. Music player
2. Radio
3. Recorder
4. Track list
0. Back
""")
        choice = input("Choose an option: ")
        match choice:
            case "1":
                print("Music player selected.")
                music()
            case "2":
                print("Radio selected.")
                music()
            case "3":
                print("Recorder selected.")
                music()
            case "4":
                print("Track list selected.")
                music()
            case "0":
                main_menu()
            case _:
                print("Invalid option, try again.")
                music()


def clock():
        print("""
===== CLOCK =====
1. Alarm clock
2. Clock settings
3. Date setting
4. Stopwatch
5. Countdown timer
6. Auto update of date and time
0. Back
""")
        choice = input("Choose an option: ")
        match choice:
            case "1":
                print("Alarm clock selected.")
                clock()
            case "2":
                print("Clock settings selected.")
                clock()
            case "3":
                print("Date setting selected.")
                clock()
            case "4":
                print("Stopwatch selected.")
                clock()
            case "5":
                print("Countdown timer selected.")
                clock()
            case "6":
                print("Auto update of date and time selected.")
                clock()
            case "0":
                main_menu()
            case _:
                print("Invalid option, try again.")
                clock()


def main_menu():
        print("""
===== NOKIA 5510 =====
1. Phone book
2. Messages
3. Chat
4. Call register
5. Tones
6. Settings
7. Call divert
8. Music
9. Games
10. Calculator
11. Reminders
12. Clock
13. Profiles
14. Services
15. SIM services
0. Exit
""")
        choice = input("Choose an option: ")
        match choice:
            case "1":
                phone_book()
            case "2":
                messages()
            case "3":
                print("Chat selected.")
                main_menu()
            case "4":
                call_register()
            case "5":
                tones()
            case "6":
                settings()
            case "7":
                print("Call divert selected.")
                main_menu()
            case "8":
                music()
            case "9":
                print("Games selected.")
                main_menu()
            case "10":
                print("Calculator selected.")
                main_menu()
            case "11":
                print("Reminders selected.")
                main_menu()
            case "12":
                clock()
            case "13":
                print("Profiles selected.")
                main_menu()
            case "14":
                print("Services selected.")
                main_menu()
            case "15":
                print("SIM services selected.")
                main_menu()
            case "0":
                print("Goodbye!")
                return
            case _:
                print("Invalid option, try again.")
                main_menu()


main_menu()
