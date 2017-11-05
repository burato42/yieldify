Feature: Test Google Keep Note creation

  As a Google Keep user
  I want to be able to create new notes
  So that I can work with those notes after creation

  Scenario: User is able to create a text note
    Given I am logged in and I am in Google Keep page
    When I click on Take a note field
    And I enter title "New Title"
    And I enter text "This is a text"
    And I press Done
    Then the new note is on the page and I can click it
    And the saved title is equal to "New Title"
    And the saved text is equal to "This is a text"

  Scenario: User is able to create a text note without text
    Given I am logged in and I am in Google Keep page
    When I click on Take a note field
    And I enter title "New Title"
    And I press Done
    Then the new note is on the page and I can click it
    And the saved title is equal to "New Title"

  Scenario: User is able to create a text note without title
    Given I am logged in and I am in Google Keep page
    When I click on Take a note field
    And I enter text "This is a text"
    And I press Done
    Then the new note is on the page and I can click it
    And the saved text is equal to "This is a text"
