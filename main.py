def main():
    print("Welcome to the email slicer ")
    print("")

    email_input = input("Enter your email address: ")

    # Slice user name and domain
    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print(f"Username: {username}")
    print(f"Domain: {domain}")
    print(f"Extension: {extension}")

main()

print("Do you want to enter another email address: y-'Yes', n-'No'")
user_response = input("")
if user_response == 'y':
  main()
elif user_response == 'n':
  print('Have a nice day!')

