## Testing 

## Manual Testing

### Testing User Stories

The website functionality with all user stories has been tested manually while logged in as testusers, site owner/admin and while not logged in. Additional tests from the user perspective have been made by a friend who created a user account for themselves. 

1. As a user I .....
    ![Instructions](documentation/screenshots/homepage.png)


### Javascript
- JavaScript
  - JavaScript was used for the time out function of django contrib messages.
    - This was tested manually. The messages displayed dissappear automatically.
 
    ![Timeout](documentation/testing/js/jstimeoutfunction.png)

  - JavaScript was used ..... 
    - This was tested manually as well. 
    - .....

    ![Image](documentation/testing/....)



### Browser Compatibility

- The page has been tested and works in different browsers.
  - Google Chrome
    ![Google Chrome](documentation/screenshots/googlechrome.png)
    ![Google Chrome Mobile](documentation/screenshots/googlechromemobile.png)

  - Firefox
    ![Firefox](documentation/screenshots/firefox.png)
    ![Firefox Tablet](documentation/screenshots/firefoxtablet.png)
  
  - Microsoft Edge
    ![Microsoft Edge](documentation/screenshots/microsoftedge.png)
    ![Microsoft Edge Mobile](documentation/screenshots/microsoftedgemobile.png)

### Responsiveness

- The project is responsive and functions on all standard screen sizes using the devtools device toolbar.

- The navigation, home page, ..... and the footer are readable and easy to understand.

  -  Google Chrome Desktop

    ![Google Chrome](documentation/screenshots/googlechrome.png)

  - Google Chrome Mobile

    ![Google Chrome Mobile](documentation/screenshots/googlechromemobile.png)

  - Firefox Desktop

    ![Firefox](documentation/screenshots/firefox.png)

  - Firefox Tablet

    ![Firefox Tablet](documentation/screenshots/firefoxtablet.png)
  
  - Microsoft Edge Desktop

    ![Microsoft Edge](documentation/screenshots/microsoftedge.png)
  
  - Microsoft Edge Mobile

    ![Microsoft Edge Mobile](documentation/screenshots/microsoftedgemobile.png)

## Color Testing

- All colors have been tested with a contrast checker. 
  - Contrast test # against #. (main background color against font color)
  ![Adobe Color Test Light Blue](documentation/screenshots/contrastcheck.png)

## Validator Testing 

- PEP8

  - No errors were returned from [PEP8online.com](http://pep8online.com/).

    <details>
    <summary>Click to expand to view the PEP8 testing</summary>
 
      - ..... app

        urls.py
        
        ![urls.py](documentation/testing/pep8/aboutme/pep8aboutmeurls.png)

        views.py

        ![views.py](documentation/testing/pep8/aboutme/pep8aboutmeviews.png)

      - ..... app

        admin.py

        ![admin.py](documentation/testing/pep8/comments/pep8commentsadmin.png)

        forms.py

        ![forms.py](documentation/testing/pep8/comments/pep8commentsforms.png)

        models.py

        ![models.py](documentation/testing/pep8/comments/pep8commentsmodels.png)

        urls.py

        ![urls.py](documentation/testing/pep8/comments/pep8commentsurls.png)

        views.py

        ![views.py](documentation/testing/pep8/comments/pep8commentsviews.png)


      - main app languageschool

        urls.py

        ![urls.py](documentation/testing/pep8/travelblog/pep8travelblogurls.png)

    </details>

- HTML

  - No errors were returned when passing through the official [W3C validator](https://validator.w3.org/)

    <details>
    <summary>Click to expand to view the HTML testing</summary>

      - Home

        [home W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftravelblogproject.herokuapp.com%2F)

        ![homepage](documentation/testing/html/home/htmlhome.png)
        

      - Contact

        [contact W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftravelblogproject.herokuapp.com%2Fcontact%2F)

        ![contact](documentation/testing/html/contact/htmlcontact.png)
      



      - Account

        login.html

        [login W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftravelblogproject.herokuapp.com%2Faccounts%2Flogin%2F)

        ![login](documentation/testing/html/account/htmllogin.png)


        signup.html

        [signup W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftravelblogproject.herokuapp.com%2Faccounts%2Fsignup%2F)

        ![signup](documentation/testing/html/account/htmlsignup.png)


        logout.html

        [logout W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftravelblogproject.herokuapp.com%2Faccounts%2Flogout%2F)  

        ![logout](documentation/testing/html/account/htmllogout.png)


    </details>

- CSS
  - No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/......)

      ![CSS validation](documentation/testing/css/cssvalidation.png)

- JavaScript
  - No errors were found when passing through [JSHint](https://jshint.com/)
  ![Timeout](documentation/testing/js/jstimeoutfunction.png)

- Accessibility
  - The page passes the accessibility test using lighthouse in devtools

    ![Lighthouse](documentation/screenshots/lighthouse.png)

## Bugs
### Fixed Bugs

The following bugs were tracked and fixed using the GitHub Issues tracker with the label of "bug".

[GitHub Issues Tracker Closed Issues](https://github.com/JulianeGampe/.....closed bugs)

- **Bug Name** - [#1](https://github.com/JulianeGampe/....)

### Remaining Bugs

- No remaining bugs that I am aware of.

---

Return to the [README](README.md) file
