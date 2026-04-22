#Will Horton
#Jack Poitras
#Davon Shields


#Creating the actual SecureBrowser class
class SecureBrowserSimulator:
    def __init__(self):
        self.back_stack = []
        self.forward_stack = []
        self.current_page = None
        self.alerts = []

        #The malicious domains/websites
        self.malicious_domains = {"malware.com", "phishing.net", "danger-site.org"}

        #Malicious key words that are common in urls
        self.malicious_keywords = {"hack", "free-money", "login-verify", "update-account"}

    # This pulls out only the domain name from the entire URL
    def extract_domain(self, url):
        # simple extraction
        return url.split("//")[-1].split("/")[0]

    # Detecting the malicious sites
    def is_malicious(self, url, domain):
        domain_check = domain in self.malicious_domains

        # Check for suspicious keywords manually
        keyword_check = False
        url_lower = url.lower()

        for keyword in self.malicious_keywords:
            if keyword in url_lower:
                keyword_check = True
                break

        return domain_check or keyword_check


    #Actually visiting URL
    def visit(self, url):
        domain = self.extract_domain(url)

        if self.current_page:
            self.back_stack.append(self.current_page)

        self.current_page = url
        self.forward_stack.clear()

        if self.is_malicious(url, domain):
            alert = f"⚠ SECURITY ALERT: Suspicious URL detected -> {url}"
            self.alerts.append(alert)
            print(alert)

        print(f"Visited: {url}")



    #Back Navigation
    def back(self):
        if self.back_stack:
            self.forward_stack.append(self.current_page)
            self.current_page = self.back_stack.pop()
            print(f"Current page: {self.current_page}")
        else:
            print("No back history available.")

    #Forward Navigation
    def forward(self):
        if self.forward_stack:
            self.back_stack.append(self.current_page)
            self.current_page = self.forward_stack.pop()
            print(f"Current page: {self.current_page}")
        else:
            print("No forward history available.")

    #Showing the actual history
    def history(self):
        print("\n--- BROWSER HISTORY ---")
        print("Back stack:", self.back_stack)
        print("Current page:", self.current_page)
        print("Forward stack:", self.forward_stack)
        print("-----------------------\n")

    #Showing the security alerts
    def show_alerts(self):
        print("\n--- SECURITY ALERTS ---")
        if self.alerts:
            for alert in self.alerts:
                print(alert)
        else:
            print("No security alerts.")
        print("-----------------------\n")


#Running the complete program
def run_simulator():
    browser = SecureBrowserSimulator()

    print("Secure Browser Simulator Started")
    print("Commands: visit <url>, back, forward, history, alerts, exit")

    #Infinite loop to keep the program running until user exits
    while True:
        command = input(">> ").strip()

        #Splits string into 2 parts  1) visit 2) the actual url
        if command.startswith("visit "):
            url = command.split(" ", 1)[1]
            browser.visit(url)

        elif command == "back":
            browser.back()

        #Go forward
        elif command == "forward":
            browser.forward()

        #Show History
        elif command == "history":
            browser.history()

        #Show security alerts (malicious sites, etc.)
        elif command == "alerts":
            browser.show_alerts()

        #Exit program
        elif command == "exit":
            print("Exiting browser...")
            break
        #If something unexpected is typed
        else:
            print("Invalid command.")


#Start program (main function)
run_simulator()