Feature: Test Feature

  @test1
  Scenario: Login Functionality
    Given user open web site
    When user click login menu
    And user entre username and email address
    And user click login button
    Then success message
    And user select gender
    And user set password
    And user set birth info
    And user select an option
    And user set name info
    And user set address info
    And user click button1