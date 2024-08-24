class Customer:
    def __init__(self, customer_id, name, party_size, vip=False):
        self.customer_id = customer_id
        self.name = name
        self.party_size = party_size
        self.vip = vip
        self.status = "Waiting"

    def seat(self):
        self.status = "Seated"
        print(f"Customer {self.name} (Party of {self.party_size} is now seated.)")

    def cancel(self):
        self.status = "Canceled"
        print(
            f"Customer {self.name} (Party of {self.party_size} has canceled their reservation.)"
        )
