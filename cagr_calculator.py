# Financial Analysis Tools - CAGR Calculator
# Author: Praveen
# Description: Calculates Compound Annual Growth Rate for investments

def calculate_cagr(start_value, end_value, years):
    """
    Calculates the Compound Annual Growth Rate (CAGR).
    
    Formula: (End Value / Start Value) ^ (1 / n) - 1
    """
    if start_value <= 0 or years <= 0:
        return "Error: Investment and years must be positive numbers."
    
    cagr = (end_value / start_value) ** (1 / years) - 1
    return cagr * 100  # Convert to percentage

# --- Main Execution ---
if __name__ == "__main__":
    print("--- CAGR Financial Calculator ---")
    
    try:
        # Taking user input
        pv = float(input("Enter Initial Investment Value (PV): "))
        fv = float(input("Enter Final Investment Value (FV): "))
        n = float(input("Enter Number of Years (n): "))
        
        # Calculation
        result = calculate_cagr(pv, fv, n)
        
        # Display Result
        if isinstance(result, str):
            print(result)
        else:
            print(f"The Compound Annual Growth Rate is: {result:.2f}%")
            
            # Analyst Insight
            if result > 12:
                print("Analysis: This is a high-growth investment (beats average market returns).")
            elif result > 6:
                print("Analysis: This is a moderate growth investment.")
            else:
                print("Analysis: This returns below inflation rates.")
                
    except ValueError:
        print("Invalid input! Please enter numeric values.")
