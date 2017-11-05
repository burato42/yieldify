# Yieldify test task

This is the solution of test task for Software Engineer in Test position.
I've taken Google Keep App as an application under test.
As Yieldify uses Cucumber for tests I decided to use Gherkin style tests as well.
All test cases are written using Gherkin. I have automated only basic tests.

Python 3.6 has been chosen as a programming language for automated tests implementation and _behave_ as a BDD framework.
To interact with a browser I have used Selenium Webdriver.

## Content

- Test Cases
- Installation
- Test running

## Test Cases

### Prerequisites
It's needed to have an Google account to start testing. You can use these credentials:
```
login: test.yieldify.task@gmail.com
password: testyieldify2013
```

After login to the account the tests could be executed.
I understand that the number of even very simple test cases could be very big so I've decided not to cover all possible scenarios
To decrease number of tests, I've checked some additional features (reminders, colllaborators etc.) separately only for text notes.
For list notes I add these features during one test. 
### List of test cases
```

Feature: Test Google Keep text note creation
  As a Google Keep user
  I want to be able to create new notes
  So that I can work with those notes after creation

  
  Scenario Outline: User is able to create a text note
    Given I am logged in and I am in Google Keep page
    When I click on Take a note field
    And I enter title <title>
    And I enter text <text>
    And I press Done
    Then the new note is on the page and I can click it
    And the saved title is equal to <title>
    And the saved text is equal to <text>

  
    Examples: New notes
      | title     | text           |
      | New Title | This is a text |
      | New Title |                |
      |           | This is a text |

  
  Scenario: User is not able to create note with very long title and text
    Given I am logged in and I am in Google Keep page
    When I click on Take a note field
    And I enter title with 1000 symbols
    And I enter text with 20000 symbols
    And I press Done
    Then the new note is on the page and I can click it
    And the saved title has length 999
    And the saved text has length 19999

  
  Scenario: User is able to create a text note with maximum possible text and title length
    Given I am logged in and I am in Google Keep page
    When I click on Take a note field
    And I enter title with 999 symbols
    And I enter text with 19999 symbols
    And I press Done
    Then the new note is on the page and I can click it
    And the saved title is equal to the long title
    And the saved text is equal to the long text
  
  Scenario: User is not able to create empty
    Given I am logged in and I am in Google Keep page
    When I click on Take a note field
    And I press Done
    Then the new note is not created
    
  Scenario: User is able to add picture during creation
    Given I am logged in and I am in Google Keep page
    When I click on Take a note field
    And I enter title "Test title"
    And I enter text "Test text"
    And I add a picture from the disk
    And I press Done
    Then the new note is on the page and I can click it
    And the saved title is equal to "Text title"
    And the saved text is equal to "Test text"
    And the picture is saved
  
  Scenario: User is able to add picture during creation
    Given I am logged in and I am in Google Keep page
    When I click on Take a note field
    And I enter title "Test title"
    And I enter text "Test text"
    And I add a picture from the disk
    And I press Done
    Then the new note is on the page and I can click it
    And the saved title is equal to "Text title"
    And the saved text is equal to "Test text"
    And the picture is saved
    
    
  Scenario: User is able to change note colour during creation
    Given I am logged in and I am in Google Keep page
    When I click on Take a note field
    And I enter title "Test title"
    And I enter text "Test text"
    And I change the colour to yellow
    And I press Done
    Then the new note is on the page and I can click it
    And the saved title is equal to "Text title"
    And the saved text is equal to "Test text"
    And the note colour is yellow
    
  Scenario: User is able to add collaborator during creation
    Given I am logged in and I am in Google Keep page
    When I click on Take a note field
    And I enter title "Test title"
    And I enter text "Test text"
    And I add the collaborator
    And I press Done
    Then the new note is on the page and I can click it
    And the saved title is equal to "Text title"
    And the saved text is equal to "Test text"
    And there is a collaborator symbol on the note
    And the collaborator get the email
    And the collaborator has access to this note
    
    
  Scenario: User is able to add reminder during creation
    Given I am logged in and I am in Google Keep page
    When I click on Take a note field
    And I enter title "Test title"
    And I enter text "Test text"
    And I add a reminder
    And I press Done
    Then the new note is on the page and I can click it
    And the saved title is equal to "Text title"
    And the saved text is equal to "Test text"
    And the reminder time is on the note
    And the I get a notification at right time
    
    
Feature: Test Google Keep list note creation

  As a Google Keep user
  I want to be able to create new list notes
  So that I can work with those notes after creation
  
  Scenario: User is able to create a list note
    Given I am logged in and I am in Google Keep page
    When I click on New list button
    And I enter title "Test title"
    And I enter the first list element "First element"
    And I enter the second list element "Second element"
    And I press Done
    Then the new note is on the page and I can click it
    And the saved title is equal to "Text title"
    And the first list element is equal to "First element"
    And the first list element is equal to "Second element"
    
    
Feature: Test Google Keep note with a picture creation

  As a Google Keep user
  I want to be able to create new notes with image
  So that I can work with those notes after creation
  
  Scenario: User is able to create a note with picture
    Given I am logged in and I am in Google Keep page
    When I click on New note with picture button
    And And I add a picture from the disk
    And I enter title "Test title"
    And I enter text "Test text"
    And I press Done
    Then the new note is on the page and I can click it
    And the saved title is equal to "Text title"
    And the saved text is equal to "Test text"
    And the picture is saved
    
    
Feature: Test Google keep text note edition

  As a Google Keep user
  I want to be able to edit text notes
    
  Scenario: User is able to edit text note
    Given I am logged in and I am in Google Keep page
    And there is a text note on the page
    When I click on the text note
    And I edit the title to "New Title"
    And I edit the text to "New Text"
    And I press Done
    Then the new note is on the page and I can click it
    And the saved title is equal to "New Title"
    And the saved text is equal to "New Text"
    
    
Feature: Test Google keep list note edition

  As a Google Keep user
  I want to be able to edit list notes
  
  Scenario: User is able to edit list note
    Given I am logged in and I am in Google Keep page
    And there is a list note  with two elements on the page
    When I click on the list note
    And I change the lists element order
    And I add a picture from the disk
    And I change the colour to purple
    And I add the collaborator
    And I add a reminder
    And I press Done
    Then the new note is on the page and I can click it
    And the elements in the list have new order
    And the picture is saved
    And the note colour is purple
    And there is a collaborator symbol on the note
    And the collaborator get the email
    And the collaborator has access to this note
    And the reminder time is on the note
    And the I get a notification at right time
    
  Scenario: User is able to mark list element as completed for list note
    Given I am logged in and I am in Google Keep page
    And there is a list note  with two elements on the page
    When I click on the list note
    And I click on the checkbox
    Then the list element becomes marked as completed
    
  Scenario: User is able to convert list note to text one
    Given I am logged in and I am in Google Keep page
    And there is a list note with two elements on the page
    When I open More menu
    And I click on Hide tick boxes
    Then the note is text note
    
    
Feature: Other operations

  Scenario: User is able to copy note
    Given I am logged in and I am in Google Keep page
    And there is a text note on the page
    When I open More menu
    And press Make a copy
    Then one more note with the same content appears on the page
    
  Scenario: User is able to add label to the note
    Given I am logged in and I am in Google Keep page
    And there is a text note on the page
    When I open More menu
    And press Add label
    And fill label "some label"
    Then the label appears on the note
    And the label's text is equal to "some label"
    
  Scenario: User is able to delete the note
    Given I am logged in and I am in Google Keep page
    And there is a text note on the page
    When I open More menu
    And press Delete note
    Then the note is not present on the page
    
  Scenario: User is able to archive the note
    Given I am logged in and I am in Google Keep page
    And there is a list note with two elements on the page
    When press Archive note
    Then the note is not present on the page
    And the note is present on Archive page
```

## Installation

- Install Python 3.6 (https://www.python.org/downloads/)
- Install pip if it was not installed before (https://pip.pypa.io/en/stable/installing/)
- Install Firefox browser if it was not installed before (https://www.mozilla.org/en-US/firefox/new/)
- Install git (https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- Clone project from github (https://github.com/burato42/yieldify)
- To install requirements need to execute the command `pip install -U -r requirements.txt` from project directory

## Test running

To run test need to run command 
```
behave
```
from the project directory.

Currently these tests works with Firefox only.
