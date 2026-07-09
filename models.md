1. Sports: 
    - Tennis
    - Pickleball
    - Simulator
2. Court: 
    - name = CharField, max_length=100 - e.g. "Tennis Court 1"                      Court name
    - sport = Sports Category                                                       Sports Category
    - hourly_rate = DecimalField, max_digits=8, decimal_places=2 - e.g. 800.00      Price per hour
    - is_active = BooleanField, default=True                                        Court Availability
    - created_at = DateTimeField, auto_now_add=True                                 When was that court created
3. Coach:
    - name = CharField, max_length=100 - e.g. "John Doe"                                    Coach name
    - bio = CharField, max_length=500 - e.g. "John has been coaching tennis for 10 years."  Coach bio
    - hourly_rate = DecimalField, max_digits=8, decimal_places=2 - e.g. 50.00               Price per hour
    - sports = ForeignKey to Sports Category                                                Sports Category
    - is_active = BooleanField, default=True                                                Coach Availability
    - created_at = DateTimeField, auto_now_add=True                                         When this coach is added to the system
4. Booking:
    - court = ForeignKey to Court - e.g. "Tennis Court 1"                            Court name
    - coach = ForeignKey to Coach - e.g. "John Doe"      OPTIONAL                    Coach name
    - user = ForeignKey to User - e.g. "Jane Smith"                                  User who made the booking\
    - start_time = DateTimeField - e.g. "2023-08-01 10:00:00"                        Booking start time
    - end_time = DateTimeField - e.g. "2023-08-01 11:00:00"                          Booking end time
    - sport = ForeignKey to Sports Category - e.g. "Tennis"                          Sports Category
    - total_price = DecimalField, max_digits=8, decimal_places=2 - e.g. 100.00       Total price for the booking
    - status = CharField, max_length=20 - e.g. "Confirmed, Pending"                  Booking status (Confirmed, Cancelled, Pending)
    - created_at = DateTimeField, auto_now_add=True - e.g. "2023-07-01 09:00:00"     When the booking was created
5. Activity: 
    - name = CharField, max_length=100 - e.g. "Tennis Match"                         Activity name ("Summer Club")
    - description = CharField, max_length=500                                        Activity description
    - sport = ForeignKey to Sports Category - e.g. "Tennis"                          Sports Category
    - coach = ForeignKey to Coach - e.g. "John Doe"      OPTIONAL                    Coach name
    - date = DateTimeField - e.g. "2023-08-01 10:00:00"                              Activity date and time
    - start_time = DateTimeField - e.g. "2023-08-01 10:00:00"                        Activity start time
    - end_time = DateTimeField - e.g. "2023-08-01 11:00:00"                          Activity end time
    - price = DecimalField, max_digits=8, decimal_places=2 - e.g. 100.00             Cost for the activity
    - max_participants = IntegerField - e.g. 20                                      Maximum number of participants
    - is_active = BooleanField, default=True                                         Activity Availability
    - created_at = DateTimeField, auto_now_add=True - e.g. "2023-07-01 09:00:00"     When the activity was created