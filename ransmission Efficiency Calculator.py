class TransmissionEfficiencyCalculator:
    def __init__(self, transmitted_power, line_loss):
        self.transmitted_power = transmitted_power
        self.line_loss = line_loss

    def calculate_input_power(self):
        # Input power = transmitted power + transmission losses
        input_power = self.transmitted_power + self.line_loss
        return input_power

    def calculate_efficiency(self):
        input_power = self.calculate_input_power()

        if input_power == 0:
            return 0

        efficiency = (
            self.transmitted_power / input_power
        ) * 100

        return efficiency

    def display_result(self):
        input_power = self.calculate_input_power()
        efficiency = self.calculate_efficiency()

        print("\n----- TRANSMISSION EFFICIENCY -----")

        print(
            f"Receiving Power : "
            f"{self.transmitted_power:.2f} kW"
        )

        print(
            f"Line Loss       : "
            f"{self.line_loss:.2f} kW"
        )

        print(
            f"Sending Power   : "
            f"{input_power:.2f} kW"
        )

        print(
            f"\nTransmission Efficiency : "
            f"{efficiency:.2f}%"
        )

        if efficiency >= 95:
            print("Efficiency Status : EXCELLENT")
        elif efficiency >= 90:
            print("Efficiency Status : GOOD")
        elif efficiency >= 80:
            print("Efficiency Status : MODERATE")
        else:
            print("Efficiency Status : LOW")


def main():

    print("==========================================")
    print("      TRANSMISSION EFFICIENCY CALCULATOR")
    print("==========================================")

    try:
        transmitted_power = float(
            input("\nEnter receiving-end power (kW): ")
        )

        line_loss = float(
            input("Enter transmission line loss (kW): ")
        )

        if transmitted_power <= 0 or line_loss < 0:
            print("\nPlease enter valid values.")
            return

        calculator = TransmissionEfficiencyCalculator(
            transmitted_power,
            line_loss
        )

        calculator.display_result()

    except ValueError:
        print("\nInvalid input! Please enter numerical values.")


if __name__ == "__main__":
    main()
