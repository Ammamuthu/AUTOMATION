# ===============================================================================

# First one is success full 
import subprocess

def check_database_status(username, password, hostname, port, service_name):
    command = f'sqlplus {username}/{password}@{hostname}:{port}/{service_name}'

    try:
        subprocess.run(command, check=True, shell=True)
        print(f"The database on {hostname}:{port}/{service_name} is UP.")
    except subprocess.CalledProcessError as e:
        print(f"The database on {hostname}:{port}/{service_name} is DOWN. Error: {e}")

# Example usage
check_database_status("system", "ADMIN", "localhost", "1521", "xe")
# ===============================================================================
import subprocess

def check_database_status(username, password, hostname, port, service_name):
    command = f'sqlplus {username}/{password}@{hostname}:{port}/{service_name}'

    try:
        subprocess.run(command, check=True, shell=True)
        print(f"The database on {hostname}:{port}/{service_name} is UP.")
    except subprocess.CalledProcessError as e:
        print(f"The database on {hostname}:{port}/{service_name} is DOWN. Error: {e}")

# Example usage
check_database_status("system", "ADMN", "localhost", "1521", "xe")
