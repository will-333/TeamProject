class SecureBrowserSimulator:
    def __init__(self):
        self.back_stack = []
        self.forward_stack = []
        self.current_page = None
        self.alerts = []

        #The malicious domains/websites
        self.malicious_domains = {"malware.com", "phishing.net", "danger-site.org"}

        self.malicious_keywords = {"hack", "free-money", "login-verify", "update-account"}

    #Actually visiting URL.
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

    #This pulls out only the domain name from the entire URL
    def extract_domain(self, url):
        # simple extraction
        return url.split("//")[-1].split("/")[0]

    #Detecting the malicious sites
    def is_malicious(self, url, domain):
        domain_check = domain in self.malicious_domains

        keyword_check = any(
            keyword.lower() in url.lower()
            for keyword in self.malicious_keywords
        )

        return domain_check or keyword_check

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

    while True:
        command = input(">> ").strip()

        if command.startswith("visit "):
            url = command.split(" ", 1)[1]
            browser.visit(url)

        elif command == "back":
            browser.back()

        elif command == "forward":
            browser.forward()

        elif command == "history":
            browser.history()

        elif command == "alerts":
            browser.show_alerts()

        elif command == "exit":
            print("Exiting browser...")
            break

        else:
            print("Invalid command.")


# Start program
run_simulator()