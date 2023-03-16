Feature: Search for videos

  Scenario: Search for a video using a keyword
    Given that we have gone to www.youtube.com
    When I enter "cat videos" into the search bar
    And I click the search button
    Then I should see a list of videos related to "cat videos"
    
  Scenario: Search for a video using a partial keyword
    Given that we have gone to www.youtube.com
    When I enter "cooking" into the search bar
    And I click the search button
    Then I should see a list of videos related to "cooking"
    
  Scenario: Search for a video using a misspelled keyword
    Given that we have gone to www.youtube.com
    When I enter "catt videos" into the search bar
    And I click the search button
    Then I should see a message indicating that there are no results for "catt videos"
