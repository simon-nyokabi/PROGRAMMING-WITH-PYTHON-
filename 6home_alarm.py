# HOME ALARM SYSTEM 

def security_check(is_door_open, is_system_enabled, has_key_fob):
    if (is_door_open and is_system_enabled) and not has_key_fob:
        result = " ALARM TRIGGERED"
    elif is_door_open and is_system_enabled and has_key_fob:
        result = " Welcome Home. System Disarmed" 
    elif is_door_open and not is_system_enabled:
        result = " Door opened. System inactive"
    else:
        result = "System secure"
    return result

# --- DEBUG START ---
print("--- SECURITY SYSTEM INITIALIZED ---")
print("(Please click below and type Y or N for each question)")

door = input("Is the door open? (Y/N) : ").upper() == 'Y'
system = input("Is the system enabled? (Y/N) : ").upper() == 'Y'
key = input("Is the key available? (Y/N) : ").upper() == 'Y'

status = security_check(door, system, key)

print("\n--- FINAL STATUS ---")
print(status)