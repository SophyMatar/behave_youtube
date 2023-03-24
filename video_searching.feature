 Feature: Search for videos

 Scenario: Search for a video using a keyword
    Given that we have gone to wwww.youtube.com
    When I enter "BTS music videos" into the search bar
    And I click the search button
    Then I should see a list of videos related to "BTS music videos"
    
  Scenario: Search for a video using a partial keyword
    Given that we have gone to wwww.youtube.com
    When I enter "music" into the search bar
    And I click the search button
    Then I should see a list of videos related to "music"
    
  Scenario: Search for a video using a misspelled keyword
    Given that we have gone to wwww.youtube.com
    When I enter "cobing videos" into the search bar
    And I click the search button
    Then I should see a message indicating that there are no results for "cobing videos"

