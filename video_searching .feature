Feature: Search for videos
  As a user
  I want to search for videos based on keywords
  So that I can find the videos I am interested in

  Scenario: Search for a video using a keyword
    Given I am on the YouTube homepage
    When I enter "cat videos" into the search bar
    And I click the search button
    Then I should see a list of videos related to "cat videos"
    
  Scenario: Search for a video using a partial keyword
    Given I am on the YouTube homepage
    When I enter "cooking" into the search bar
    And I click the search button
    Then I should see a list of videos related to "cooking"
    
  Scenario: Search for a video using a misspelled keyword
    Given I am on the YouTube homepage
    When I enter "catt videos" into the search bar
    And I click the search button
    Then I should see a message indicating that there are no results for "catt videos"
