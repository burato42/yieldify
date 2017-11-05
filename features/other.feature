Feature: Other operations

    Scenario: User is able to delete the note
      Given I am logged in and I am in Google Keep page
      And there is a text note on the page
      When I open More menu
      And press Delete note
      Then the note is not present on the page