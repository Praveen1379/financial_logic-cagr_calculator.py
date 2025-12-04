# Financial Analysis Tools - CAGR Calculator

def calculate_cagr(start_value, end_value, years):
    # Logic to calculate growth rate
    if start_value <= 0 or years <= 0:
        return None
    
    # Formula: (FV / PV) ^ (1/n) - 1
    cagr = (end_value / start_value) ** (1 / years) - 1
    return cagr * 100

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    print("--- CAGR Financial Calculator ---")
    
    try:
        # STEP 1: Inputs
        pv = float(input("Enter Initial Investment (PV): "))
        fv = float(input("Enter Final Investment (FV): "))
        n = float(input("Enter Years (n): "))

        # STEP 2: Calculate
        result = calculate_cagr(pv, fv, n)

        # STEP 3: Output
        if result is None:
            print("Error: Inputs must be positive numbers.")
        else:
            # Using .format() to prevent version errors
            print("The CAGR is: {:.2f}%".format(result))
            
            # Analysis Logic
            if result > 12:
                print("Analysis: High Growth (Beats Market)")
            elif result > 6:
                print("Analysis: Moderate Growth")
            else:
                print("Analysis: Low Growth (Inflation Risk)")
                
    except ValueError:
        print("Error: Please enter valid numbers only.")
    except Exception as e:
        print("An error occurred:", e)
