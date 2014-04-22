# Eclipse, ADK etc setup on Ubuntu 13.04

Use Oracle JDK 6.
Use Eclipse, but install ADK plugins through "Help..."
Install relevant tools and SDKs using ~/android-sdks/tools 

# Application components
Implemented as Java Classes
Android instatiates and runs these as needed, each has its own purpose and API.

## Activity
Main class users see when they run an app
Provides a GUI, allows users to receive and give info
Activity should provide a single focused thing the user can do - as a rule
    Phone application has multiple tabs

## Services
Run in BG
    perform long-running ops
    support interaction w/remote apps


## Broadcast receivers
listen for and respond to events
    subscriber in publish/subscribe
    events represented by the intent class and then broadcast
    receives and responds to broadcast event


## Content providers
allow apps to store and share data accross apps
    database-style interface
    handles interprocess communication

# Development
## Define resources
Code, non-code
non-code
    String, string arrays etc

# The Activity Class
## The Activity Class
    Provides a visual interface for user interaction
    Each activity typically supports one focused thing a user can do, such as
        Viewing and email address
        Showing a login screen
    Applications often comprise several activites
    Navigation through Activities
        Android supports navigation in several ways
            tasks
            the Task Backstack
            Suspending and Resuming Activities
    
    Tasks
        A Task is a set of related Activities
        These related activities don't have to be part of the same application 
        Most tasks start at the home screen
        See: http://developer.android.com/guide/topics/fundamentals/tasks-and-back-stack.html

## The Task Backstack
    When an Activity is launched, it goes on top of the backstack
    When the Activity is destroyed, it is popped off the backstack
## The Activity Lifecycle
    Activities are created, suspended
    Resumed and destroyed as necessary when an application executes
    Some of these actions depend on user behavior
    Some depend on Android
## Starting Activities
## Handling Configuration Changes

