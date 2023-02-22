import appJar


# Initialize the app
app = appJar.gui("Assetto Corsa Car Tracker")

# Connect to the Assetto Corsa server


# Define a function to update the car's position
def update_position():
    import acServer
    print("importing server")
    server = acServer.connect("127.0.0.1", 9000)
    position = server.getPosition()

    # Display the car's position on the map
    # (replace this with your own map display code)
    print("Car position:", position)

# Create a button to start tracking the car
def start_tracking():
    app.setPollTime(100)
    app.registerEvent(update_position)

# Add the button to the app
app.addButtons(["Start Tracking"], [start_tracking])

# Start the app
app.go()
