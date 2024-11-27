
import mysql.connector

def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="final"
    )

def execute_query(cursor, query, data=None):
    try:
        if data:
            cursor.execute(query, data)
        else:
            cursor.execute(query)
        print("Operation successful.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def menu():
    print("Car Sales Database CLI")
    print("1. Operations on client data")
    print("2. Operations on store data")
    print("3. Operations on staff data")
    print("4. Operations on vehicle data")
    print("5. Operations on make data")
    print("6. Operations on client_account data")
    print("7. Operations on vehicle_performance data")
    print("8. Operations on sale data")
    print("9. Operations on rental data")
    print("10. Operations on commission data")
    print("11. Perform queries on the data")
    print("12. Exit")

def client(cursor):
    choice = input("Operation to perform(insert/update/delete): ")
    if choice == 'insert':
        name = input("Enter client's name:").strip()
        salary = input("Enter client's salary:").strip()
        purchased = 1
        query = """ INSERT INTO client (name,salary,purchased) VALUES (%s,%s,%s) """
        execute_query(cursor,query,(name,salary,purchased))
    elif choice == 'delete':
        id = input("Enter client id to delete:").strip()
        query = """ DELETE FROM client WHERE client_id = (%s)"""
        execute_query(cursor,query,(id,))
    elif choice == 'update':
        id = input("Enter client id to update:").strip()
        salary = input("Enter new salary:").strip()
        query = """ UPDATE client set salary = (%s) WHERE client_id = (%s)"""
        execute_query(cursor,query,(salary,id))
    else:
        print("Invalid choice. Try again.")

def staff(cursor):
    choice = input("Operation to perform(insert/update/delete): ")
    if choice == 'insert':
        name = input("Enter staff's name:").strip()
        store_id = input("Enter store_id:").strip()
        hire_date = input("Enter hire_date:").strip()
        query = """ INSERT INTO staff (name,store_id,hire_date) VALUES (%s,%s,%s) """
        execute_query(cursor,query,(name,store_id,hire_date))
    elif choice == 'delete':
        id = input("Enter staff id to delete:").strip()
        query = """ DELETE FROM staff WHERE staff_id = (%s)"""
        execute_query(cursor,query,(id,))
    elif choice == 'update':
        id = input("Enter staff id to update:").strip()
        store_id = input("Enter store id to change to:").strip()
        query = """ UPDATE staff set store_id = (%s) WHERE staff_id = (%s)"""
        execute_query(cursor,query,(store_id,id))
    else:
        print("Invalid choice. Try again.")

def store(cursor):
    choice = input("Operation to perform(insert/delete): ")
    if choice == 'insert':
        print("Enter store details to insert:")
        store_id = input("Store ID: ").strip()
        brand = input("Brand: ").strip()
        location_name = input("Location Name: ").strip()
        location_number = input("Location Number: ").strip()
        location_type = input("Location Type: ").strip()
        address = input("Address: ").strip()
        country = input("Country: ").strip()
        city = input("City: ").strip()
        state = input("State: ").strip()
        postal_code = input("Postal Code: ").strip()
        latitude = float(input("Latitude: ").strip())
        longitude = float(input("Longitude: ").strip())
               
        query = """
            INSERT INTO store (
                store_id, brand, location_name, location_number, location_type,
                address, country, city, state, postal_code, latitude, longitude
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        params = (store_id, brand, location_name, location_number, location_type,
                address, country, city, state, postal_code, latitude, longitude)

        execute_query(cursor, query, params)
    elif choice == "delete":
        city = input("Enter the city name for which the stores should be deleted: ").strip()
        query = """DELETE FROM store WHERE city = %s"""
        execute_query(cursor, query, (city,))
    else:
        print("Invalid choice. Try again.")

def vehicle(cursor):
    choice = input("Operation to perform(insert/delete/update): ")
    if choice == 'insert':
        make_id = input("Make ID: ").strip()
        model = input("Model: ").strip()
        year = input("Year: ").strip()
        
        while not year.isdigit() or len(year) != 4:
            print("Invalid year. Please enter a valid 4-digit year.")
            year = input("Year: ").strip()
        
        price = input("Price: ").strip()
        while True:
            try:
                price = float(price)
                break
            except ValueError:
                print("Invalid price. Please enter a numeric value.")
                price = input("Price: ").strip()
        
        commission_rate = input("Commission Rate: ").strip()
        while True:
            try:
                commission_rate = float(commission_rate)
                break
            except ValueError:
                print("Invalid commission rate. Please enter a numeric value.")
                commission_rate = input("Commission Rate: ").strip()

        query = """
            INSERT INTO vehicle (make_id, model, year, price, commission_rate)
            VALUES (%s, %s, %s, %s, %s)
        """
        params = (make_id, model, year, price, commission_rate)

        execute_query(cursor, query, params)

    elif choice == "delete":
        vehicle_id = input("Enter the Vehicle ID to delete: ").strip()
        query = "DELETE FROM vehicle WHERE vehicle_id = %s"
        execute_query(cursor, query, (vehicle_id,))

    elif choice == "update":  
        vehicle_id = input("Enter the Vehicle ID to update the price: ").strip()
        new_price = input("Enter the new price: ").strip()
        # Validate the new price
        while True:
            try:
                new_price = float(new_price)
                break
            except ValueError:
                print("Invalid price. Please enter a numeric value.")
                new_price = input("Enter the new price: ").strip()

        query = "UPDATE vehicle SET price = %s WHERE vehicle_id = %s"
        execute_query(cursor, query, (new_price, vehicle_id))

    else:
        print("Invalid choice. Try again.")
def make(cursor):
    choice = input("Operation to perform(insert/update): ")
    if choice == 'insert':
        make_name = input("Enter the Make Name to insert: ").strip()
        if not make_name:
            print("Make Name cannot be empty.")
            return
        query = "INSERT INTO make (make_name) VALUES (%s)"
        execute_query(cursor, query, (make_name,))

    elif choice == 'update':
        make_id = input("Enter the Make ID to update: ").strip()
    
        if not make_id.isdigit():
            print("Invalid Make ID. Please enter a numeric value.")
            return

        new_make_name = input("Enter the new Make Name: ").strip()
        
        if not new_make_name:
            print("New Make Name cannot be empty.")
            return

        query = "UPDATE make SET make_name = %s WHERE make_id = %s"
        execute_query(cursor, query, (new_make_name, make_id))

    else:
        print("Invalid choice. Try again.")

def client_account(cursor):
    choice = input("Operation to perform(insert/update): ")
    if choice == 'insert':
        client_id = input("Enter Client ID: ").strip()
        balance = input("Enter Balance: ").strip()
        created_date = input("Enter Created Date (YYYY-MM-DD): ").strip()
        status = input("Enter Status (Active/Inactive/Suspended): ").strip()

        while True:
            try:
                balance = float(balance)
                break
            except ValueError:
                print("Invalid balance. Please enter a numeric value.")
                balance = input("Enter Balance: ").strip()

        import datetime
        try:
            datetime.datetime.strptime(created_date, '%Y-%m-%d')
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD.")
            return

        if not status:
            print("Status cannot be empty.")
            return

        query = """
            INSERT INTO client_account(client_id, balance, created_date, status)
            VALUES (%s, %s, %s, %s)
        """
        execute_query(cursor, query, (client_id, balance, created_date, status))
        
    elif choice == 'update':
        print("Choose the operation you want to perform:")
        print("1. Update Account Status")
        print("2. Update Account Balance")
        choice = input("Enter your choice (1 or 2): ").strip()

        if choice == "1":
            account_id = input("Enter Account ID to update the status: ").strip()
            new_status = input("Enter the new Status (Active/Inactive/Suspended): ").strip()

            if not new_status:
                print("Status cannot be empty.")
                return

            query = "UPDATE client_account SET status = %s WHERE account_id = %s"
            execute_query(cursor, query, (new_status, account_id))

        elif choice == '2':
            account_id = input("Enter Account ID to update the balance: ").strip()
            new_balance = input("Enter the new Balance: ").strip()

            while True:
                try:
                    new_balance = float(new_balance)
                    break
                except ValueError:
                    print("Invalid balance. Please enter a numeric value.")
                    new_balance = input("Enter the new Balance: ").strip()

            query = "UPDATE client_account SET balance = %s WHERE account_id = %s"
            execute_query(cursor, query, (new_balance, account_id))
    
        else:
            print("Invalid choice. Please select 1 or 2.")

    else:
        print("Invalid choice. Try again.")

def vehicle_performance(cursor):
    choice = input("Operation to perform(insert/update/delete): ")
    if choice == 'insert':
        vehicle_id = input("Enter Vehicle ID: ").strip()
        rating = input("Enter Rating (0-10): ").strip()
        trips_taken = input("Enter Trips Taken: ").strip()
        review_count = input("Enter Review Count: ").strip()

        while True:
            try:
                rating = float(rating)
                if rating >= 0 and rating <= 10:
                    break
                else:
                    print("Rating must be between 0 and 10.")
                    rating = input("Enter Rating (0-10): ").strip()
            except ValueError:
                print("Invalid rating. Please enter a numeric value.")
                rating = input("Enter Rating (0-10): ").strip()

        try:
            trips_taken = int(trips_taken)
            review_count = int(review_count)
        except ValueError:
            print("Trips Taken and Review Count must be numeric values.")
            return

        query = """
            INSERT INTO vehicle_performance (vehicle_id, rating, trips_taken, review_count)
            VALUES (%s, %s, %s, %s)
        """
        execute_query(cursor, query, (vehicle_id, rating, trips_taken, review_count))

    elif choice == 'delete':
        performance_id = input("Enter Performance ID to delete: ").strip()

        query = "DELETE FROM vehicle_performance WHERE performance_id = %s"
        execute_query(cursor, query, (performance_id,))

    elif choice == 'update':
        print("Choose the field you want to update:")
        print("1. Update Rating")
        print("2. Update Trips Taken")
        print("3. Update Review Count")
        choice = input("Enter your choice (1, 2, or 3): ").strip()

        performance_id = input("Enter Performance ID to update: ").strip()

        if choice == "1":
            new_rating = input("Enter the new Rating (0-10): ").strip()

            while True:
                try:
                    new_rating = float(new_rating)
                    if new_rating >= 0 and new_rating <= 10:
                        break
                    else:
                        print("Rating must be between 0 and 10.")
                        new_rating = input("Enter the new Rating (0-10): ").strip()
                except ValueError:
                    print("Invalid rating. Please enter a numeric value.")
                    new_rating = input("Enter the new Rating (0-10): ").strip()

            query = "UPDATE vehicle_performance SET rating = %s WHERE performance_id = %s"
            execute_query(cursor, query, (new_rating, performance_id))
        
        elif choice == "2":
            new_trips_taken = input("Enter the new Trips Taken: ").strip()

            try:
                new_trips_taken = int(new_trips_taken)
            except ValueError:
                print("Trips Taken must be a numeric value.")
                return

            query = "UPDATE vehicle_performance SET trips_taken = %s WHERE performance_id = %s"
            execute_query(cursor, query, (new_trips_taken, performance_id))
        
        elif choice == "3":
            new_review_count = input("Enter the new Review Count: ").strip()

            try:
                new_review_count = int(new_review_count)
            except ValueError:
                print("Review Count must be a numeric value.")
                return

            query = "UPDATE vehicle_performance SET review_count = %s WHERE performance_id = %s"
            execute_query(cursor, query, (new_review_count, performance_id))
        
        else:
            print("Invalid choice. Please select 1, 2, or 3.")
    else:
        print("Invalid choice. Try again.")

def sale(cursor):
    choice = input("Operation to perform(insert/delete): ")
    if choice == 'insert':
        vehicle_id = input("Enter Vehicle ID: ").strip()
        client_id = input("Enter Client ID: ").strip()
        staff_id = input("Enter Staff ID: ").strip()
        sale_price = input("Enter Sale Price: ").strip()
        commission_rate = input("Enter Commission Rate (e.g., 0.05 for 5%): ").strip()
        sale_date = input("Enter Sale Date (YYYY-MM-DD): ").strip()

        try:
            sale_price = int(sale_price)
        except ValueError:
            print("Sale Price must be a numeric value.")
            return

        try:
            commission_rate = float(commission_rate)
        except ValueError:
            print("Commission Rate must be a numeric value.")
            return

        try:
            from datetime import datetime
            datetime.strptime(sale_date, "%Y-%m-%d")
        except ValueError:
            print("Sale Date must be in the format YYYY-MM-DD.")
            return

        query = """
            INSERT INTO sale (vehicle_id, client_id, staff_id, sale_price, commission_rate, sale_date)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        execute_query(cursor, query, (vehicle_id, client_id, staff_id, sale_price, commission_rate, sale_date))

    elif choice == 'delete':
        sale_id = input("Enter Sale ID to delete: ").strip()

        try:
            sale_id = int(sale_id)
        except ValueError:
            print("Sale ID must be a numeric value.")
            return

        query = "DELETE FROM sale WHERE sale_id = %s"
        execute_query(cursor, query, (sale_id,))
    
    else: 
        print("Invalid choice. Try again.")

def rental(cursor):
    choice = input("Operation to perform(insert/update/delete): ")
    if choice == 'insert':
        vehicle_id = input("Enter Vehicle ID: ").strip()
        client_id = input("Enter Client ID: ").strip()
        rental_rate = input("Enter Rental Rate: ").strip()
        rental_length = input("Enter Rental Length (in days): ").strip()
        start_date = input("Enter Start Date (YYYY-MM-DD): ").strip()
        start_time = input("Enter Start Time (HH:MM:SS): ").strip()
        return_date = input("Enter Return Date (YYYY-MM-DD): ").strip()
        return_time = input("Enter Return Time (HH:MM:SS): ").strip()

        try:
            rental_rate = int(rental_rate)
        except ValueError:
            print("Rental Rate must be a numeric value.")
            return

        try:
            rental_length = int(rental_length)
        except ValueError:
            print("Rental Length must be a numeric value.")
            return

        from datetime import datetime
        try:
            datetime.strptime(start_date, "%Y-%m-%d")
            datetime.strptime(return_date, "%Y-%m-%d")
            datetime.strptime(start_time, "%H:%M:%S")
            datetime.strptime(return_time, "%H:%M:%S")
        except ValueError:
            print("Invalid date or time format. Please use YYYY-MM-DD for dates and HH:MM:SS for times.")
            return

        query = """
            INSERT INTO rental (vehicle_id, client_id, rental_rate, rental_length, start_date, start_time, return_date, return_time)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        execute_query(cursor, query, (vehicle_id, client_id, rental_rate, rental_length, start_date, start_time, return_date, return_time))

    elif choice == 'update':
        rental_id = input("Enter Rental ID to update: ").strip()
        new_rental_rate = input("Enter the new Rental Rate: ").strip()

        try:
            rental_id = int(rental_id)
            new_rental_rate = int(new_rental_rate)
        except ValueError:
            print("Rental ID and Rental Rate must be numeric values.")
            return

        query = "UPDATE rental SET rental_rate = %s WHERE rental_id = %s"
        execute_query(cursor, query, (new_rental_rate, rental_id))
    elif choice == 'delete':
        rental_id = input("Enter Rental ID to delete: ").strip()
        query = "DELETE FROM rental WHERE rental_id = %s"
        execute_query(cursor, query, (rental_id,))
    else: 
        print("Invalid choice. Try again.")

def commission(cursor):
    choice = input("Operation to perform(insert/update/delete): ")
    if choice == 'insert':
        staff_id = input("Enter Staff ID: ").strip()
        sale_id = input("Enter Sale ID: ").strip()
        amount = input("Enter Commission Amount: ").strip()
        try:
            staff_id = int(staff_id)
            sale_id = int(sale_id)
        except ValueError:
            print("Staff ID and Sale ID must be numeric values.")
            return

        try:
            amount = float(amount)
        except ValueError:
            print("Amount must be a numeric value.")
            return
        query = """
            INSERT INTO commission (staff_id, sale_id, amount)
            VALUES (%s, %s, %s)
        """
        execute_query(cursor, query, (staff_id, sale_id, amount))

    elif choice == 'update':
        commission_id = input("Enter Commission ID to update: ").strip()
        new_amount = input("Enter the new Commission Amount: ").strip()
        try:
            commission_id = int(commission_id)
            new_amount = float(new_amount)
        except ValueError:
            print("Commission ID must be numeric and Amount must be a valid number.")
            return
        query = "UPDATE commission SET amount = %s WHERE commission_id = %s"
        execute_query(cursor, query, (new_amount, commission_id))

    elif choice == 'delete':
        commission_id = input("Enter Commission ID to delete: ").strip()

        try:
            commission_id = int(commission_id)
        except ValueError:
            print("Commission ID must be a numeric value.")
            return

        query = "DELETE FROM commission WHERE commission_id = %s"
        execute_query(cursor, query, (commission_id,))
    else: 
        print("Invalid choice. Try again.")    

def execute_and_print_query(cursor, query):
    try:
        cursor.execute(query)
        results = cursor.fetchall()  
        if results:
            for row in results:
                print(row)  
        else:
            print("No results found.")
    except Exception as e:
        print(f"An error occurred: {e}")    

db = connect_to_db()
cursor = db.cursor()
while True:
    menu()
    choice = input("Enter choice: ")
    if choice == "1":
        client(cursor)
    elif choice == "2":
        store(cursor)
    elif choice == "3":
        staff(cursor)
    elif choice == "4":
        vehicle(cursor)
    elif choice == '5':
        make(cursor)
    elif choice == '6':
        client_account(cursor)
    elif choice == '7':
        vehicle_performance(cursor)
    elif choice == '8':
        sale(cursor)
    elif choice == '9':
        rental(cursor)
    elif choice == '10':
        commission(cursor)
    elif choice == '11':
        query = input("Type the query you want to execute: ")
        execute_and_print_query(cursor, query)
    elif choice == "12":
        db.commit()
        cursor.close()
        db.close()
        print("Databse closed")
        break
    else:
        print("Invalid choice. Try again.")
    db.commit()

