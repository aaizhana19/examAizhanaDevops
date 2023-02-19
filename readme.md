Task: Create the new table Booking with the following columns:
- id (int,primary key)
- name (varchar)
- type (varchar)
- price_for_nights (integer) 
- rooms (integer) 
- numof_nights (integer) 
- numof_travelers (integer) 
- status (varchar) default "free"
- check_in (date) default "10,02,2023"
- check_out (date) default now
- amount (int) 

Services:
1. Create new reservation every minute.
2. Update all new reservations and multiplies price_for_nights * num_ofnights * numof_travelers and change the status to the "booked"
3. Update all reservations and change the status "finish" where status is "booked"
4. Get the all reservations monitoring
