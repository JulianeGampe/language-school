## Testing 

## Manual Testing

### Testing User Stories

The website functionality with all user stories has been tested manually while logged in as testusers or admin and while not logged in. 

#### Student
##### Viewing and Navigation
1.	As a student I can see the home page so that I get an overview of what I can learn.
    ![Homepage Part 1](documentation/screenshots/homepageone.png)
    ![Homepage Part 2](documentation/screenshots/homepagetwo.png)
2.	As a student I can see and browse all available courses so that I can make a choice on which one to book.
    ![Courses](documentation/screenshots/courses.png)
3.	As a student I can see the details of an individual course so that I can see all necessary information including a course description.
    ![Coursedetail Student](documentation/screenshots/coursedetailstudent.png)
4.	As a student I can see general information about the offered courses and language levels so that I can decide better which course is the right one for me.
    ![Course Information](documentation/screenshots/courseinformation.png)
5.	As a student I can see information about the teachers so that I can reassure myself about the quality of the offered classes.
    ![Teachers](documentation/screenshots/teachers.png)
6.	As a student I can see contact details of the language school so that I can get in touch in case I have additional questions.
    ![Contact](documentation/screenshots/contact.png)
    - A contact form can be filled in. Valid information has to be provided before sending.
        ![Contact Form Test](documentation/screenshots/contactformtest.png)
7.	As a student I can see a link to the schools Facebook page so that I can connect with them via social media.
    ![Footer](documentation/screenshots/footer.png)
8.	As a student I can sign up for the schools newsletter so that I can receive newsletters with up-to-date information.
    ![Homepage Part 2](documentation/screenshots/homepagetwo.png)


##### User account
9.	As a student I can register for an account so that I am able to view my profile.
    ![Sign Up](documentation/screenshots/signup.png)
    - The signup was tested with testaccounts.
    - It is not possible to sign up with missing or incorrect fields.
        ![Sign Up Test](documentation/screenshots/signuptest.png)
    - After signing up an email is sent to verify the email address.
        ![Sign Up Email](documentation/screenshots/signupemail.png)
        ![Sign Up Email Confirmation](documentation/screenshots/signupemailconfirm.png)
    - After signup it is possible to login and access the My Profile Page
        ![Sign Up Profile](documentation/screenshots/signupmyprofile.png)
10.	As a student I will receive a confirmation email after registering so that I know that my account registration was successful. 
    ![Sign Up Email Sent](documentation/screenshots/signupemailsent.png)
11.	As a student I can login and logout of my account so that I can access my personal information.
    ![Sign In](documentation/screenshots/signin.png)
    ![Sign Out](documentation/screenshots/signout.png)
    - All necessary fields have to be filled correctly to sign in.
        ![Sign In Test](documentation/screenshots/signintest.png)
12.	As a student I have a personalized user profile so that I can view the courses that I have booked.
    ![Sign In Test](documentation/screenshots/profile.png)
13.	As a student I can recover my account password so that I can access my account in case I forgot my password.
    - A Forgot Password Link is available on the login page.
        ![Sign In](documentation/screenshots/signin.png)
    - When clicked, an email can be sent with recovery information.
        ![Password Reset](documentation/screenshots/passwordreset.png)

##### Sorting and Searching
14.	As a student I can sort the list of all available courses by level so that I can see courses matching my current language level.
    - A drop down menu to sort the courses is available
        ![Sorting](documentation/screenshots/sortingandsearching.png)
    - Courses can be sorted by level
        ![Level](documentation/screenshots/sortlevel.png)
15.	As a student I can sort the list of all available courses by course format so that I can quickly choose courses from my preferred course format.
    - A drop down menu to sort the courses is available
        ![Sorting](documentation/screenshots/sortingandsearching.png)
    - Courses can be sorted by level
        ![Format](documentation/screenshots/sortformat.png)
16.	As a student I can sort the list of all available courses by the start date of the course so that I can choose a course that starts on a suitable date.
    - A drop down menu to sort the courses is available
        ![Sorting](documentation/screenshots/sortingandsearching.png)
    - Courses can be sorted by date
        ![Date](documentation/screenshots/sortstartdate.png)
17.	As a student I can sort the list of all available courses by the weekday on which the course will take place so that I can find a course that fits my schedule.
    - A drop down menu to sort the courses is available
        ![Sorting](documentation/screenshots/sortingandsearching.png)
    - Courses can be sorted by weekday
        ![Weekday](documentation/screenshots/sortweekday.png)
18.	As a student I can search for a course by level or course format to find a specific course that I want to book.
    - A search bar to search for courses is available
        ![Sorting](documentation/screenshots/sortingandsearching.png)
    - Searching for level is possible
        ![Search Level](documentation/screenshots/searchlevel.png)
    - Searching for format is possible
        ![Search Level](documentation/screenshots/searchformat.png)
19.	As a student I can easily see what I have searched for so that I can quickly decide if my desired course is available.
    - The number of search results is displayed together with the search term below the search bar
        ![Search Level](documentation/screenshots/searchformat.png)


##### Purchase and Checkout
20.	As a student I can see the course(s) that I have in my shopping bag so that I can see which course(s) I am about to purchase.
    ![Shopping Bag](documentation/screenshots/shoppingbag.png)
21.	As a student I can remove a chosen course from my shopping bag so that I can make changes to my purchase before I checkout.
    - A Remove button is available next to the bag item and it removes the course from the bag when clicked
        ![Remove Course](documentation/screenshots/removecourse.png)
22.	As a student I can easily enter my payment information so that I can check out quickly. 
    ![Checkout](documentation/screenshots/checkouttwo.png)
    - Correct information has to be entered.
        ![Checkout Test](documentation/screenshots/checkouttest.png)
23.	As a student I can view an order confirmation after checkout so that I can verify I have booked the correct course(s).
    ![Checkout Confirmation](documentation/screenshots/checkoutconfirmation.png)
24.	As a student I will receive an email confirmation after purchase so that I can keep the confirmation of my course(s) for my records.
    ![Checkout Confirmation Email](documentation/screenshots/checkoutconfirmationemail.png)


#### Admin
25.	As an admin I can add new courses to the website so that I can immediately offer new courses once they are organized with the teachers.
    ![Add Course](documentation/screenshots/addcourse.png)
    - Valid information has to be provided
        ![Add Course Test](documentation/screenshots/addcoursetest.png)
26.	As an admin I can edit/update a course so that I can change the status or correct any mistakes.
    - When logged in as admin, the edit button is visible on the coursedetail page
        ![Course Detail Admin](documentation/screenshots/coursedetailadmin.png)
    - The course can then be updated
        ![Edit Course](documentation/screenshots/editcourse.png)
    - Valid information has to be provided
        ![Edit Course Test](documentation/screenshots/editcoursetest.png)
27.	As an admin I can delete a course so that I can remove a course I have accidentally created.
    - When logged in as admin, the delete button is visible on the coursedetail page
        ![Course Detail Admin](documentation/screenshots/coursedetailadmin.png)
    - When clicking on it a confirmation page will be shown before final deletion
        ![Delete Course](documentation/screenshots/deletecourse.png)

#### Student + Admin
28. As a student/admin I can see messages on the screen so that I know the result of my input.
    ![Message Example One](documentation/screenshots/messageone.png)
    ![Message Example Two](documentation/screenshots/messagetwo.png)

### Javascript
- JavaScript
    - JavaScript was used for the time out function of django contrib messages.
         - This was tested manually. The messages displayed dissappear automatically.
    - JavaScript was used for the sorting dropdown on the courses page.
        - This code was taken from the Boutique Ado walkthrough project from Code Institute
        - This was tested manually as well. 
        - The sorting box works.
        ![Sorting](documentation/screenshots/sortingandsearching.png)
        ![Level](documentation/screenshots/sortlevel.png)
        ![Weekday](documentation/screenshots/sortweekday.png)
    - JavaScript was used to handle stripe payments in stripe_elements.js in the checkout app
        - This code was taken from the Boutique Ado walkthrough project from Code Institute and comes from www.stripe.com
        - This was tested manually. The checkout with stripe test credit cards works.

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

- The navigation, home page, our courses, course information, our teachers, contact, profile, shopping bag, checkout, checkout success, add/edit/delete course and the footer are readable and easy to understand.

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
  - Contrast test #E4EAF2 against #000. (main background color against font color)
  ![Adobe Color Test #E4EAF2 against #000](documentation/screenshots/contrastcheckE4EAF2.png)
  - Contrast test #B8C6D9 against #000. (navbar and footer background color against font color)
  ![Adobe Color Test #B8C6D9 against #000](documentation/screenshots/contrastcheckB8C6D9.png)
  - Contrast test #262626 against #FFF. (background color for the buttons against font color of the buttons)
  ![Adobe Color Test #262626 against #FFF](documentation/screenshots/contrastcheck262626.png)
  - Contrast test #8C0303 against #FFF. (background color for the hovered buttons against font color of the hovered buttons)
  ![Adobe Color Test #8C0303 against #FFF](documentation/screenshots/contrastcheck8C0303.png)
  - Contrast test #8C0303 against #B8C6D9. (font color of the disclaimer in the footer against footer background color)
  ![Adobe Color Test #8C0303 against #B8C6D9](documentation/screenshots/contrastcheck8C0303againstB8C6D9.png)
  - Contrast test #8C0303 against #E4EAF2. (font color of the warnings/disclaimer against the light blue background color)
  ![Adobe Color Test #8C0303 against #E4EAF2](documentation/screenshots/contrastcheck8C0303againstE4EAF2.png)
  - Contrast test #262626 against #B8C6D9. (font color of the navbar links against the navbar background color)
  ![Adobe Color Test #262626 against #B8C6D9](documentation/screenshots/contrastcheck262626againstB8C6D9.png)
  - Contrast test #262626 against #E4EAF2. (font color of the website links against the light blue background color)
  ![Adobe Color Test #262626 against #E4EAF2](documentation/screenshots/contrastcheck262626againstE4EAF2.png)

## Validator Testing 

- PEP8

  - No errors were returned from [PEP8online.com](http://pep8online.com/).

    <details>
    <summary>Click to expand to view the PEP8 testing</summary>
 
      - bag app

        urls.py
        
        ![urls.py](documentation/testing/pep8/bag/pep8bagurls.png)

        views.py

        ![views.py](documentation/testing/pep8/bag/pep8bagviews.png)

      - checkout app

        admin.py

        ![admin.py](documentation/testing/pep8/checkout/pep8checkoutadmin.png)

        forms.py

        ![forms.py](documentation/testing/pep8/checkout/pep8checkoutforms.png)

        models.py

        ![models.py](documentation/testing/pep8/checkout/pep8checkoutmodels.png)

        signals.py

        ![signals.py](documentation/testing/pep8/checkout/pep8checkoutsignals.png)

        urls.py

        ![urls.py](documentation/testing/pep8/checkout/pep8checkouturls.png)

        views.py

        ![views.py](documentation/testing/pep8/checkout/pep8checkoutviews.png)


      - contact app

        admin.py

        ![admin.py](documentation/testing/pep8/contact/pep8contactadmin.png)

        forms.py

        ![forms.py](documentation/testing/pep8/contact/pep8contactforms.png)

        models.py

        ![models.py](documentation/testing/pep8/contact/pep8contactmodels.png)

        urls.py

        ![urls.py](documentation/testing/pep8/contact/pep8contacturls.png)

        views.py

        ![views.py](documentation/testing/pep8/contact/pep8contactviews.png)

      - courseinfo app

        urls.py
        
        ![urls.py](documentation/testing/pep8/courseinfo/pep8courseinfourls.png)

        views.py

        ![views.py](documentation/testing/pep8/courseinfo/pep8courseinfoviews.png)


      - courses app

        admin.py

        ![admin.py](documentation/testing/pep8/courses/pep8coursesadmin.png)

        forms.py

        ![forms.py](documentation/testing/pep8/courses/pep8coursesforms.png)

        models.py

        ![models.py](documentation/testing/pep8/courses/pep8coursesmodels.png)

        urls.py

        ![urls.py](documentation/testing/pep8/courses/pep8coursesurls.png)

        views.py

        ![views.py](documentation/testing/pep8/courses/pep8coursesviews.png)

      - home app

        admin.py

        ![admin.py](documentation/testing/pep8/home/pep8homeadmin.png)

        forms.py

        ![forms.py](documentation/testing/pep8/home/pep8homeforms.png)

        models.py

        ![models.py](documentation/testing/pep8/home/pep8homemodels.png)

        urls.py

        ![urls.py](documentation/testing/pep8/home/pep8homeurls.png)

        views.py

        ![views.py](documentation/testing/pep8/home/pep8homeviews.png)

      - main app languageschool

        urls.py

        ![urls.py](documentation/testing/pep8/languageschool/pep8languageschoolurls.png)

        views.py

        ![views.py](documentation/testing/pep8/languageschool/pep8languageschoolviews.png)

      - profiles app

        forms.py

        ![forms.py](documentation/testing/pep8/profiles/pep8profilesforms.png)

        models.py

        ![models.py](documentation/testing/pep8/profiles/pep8profilesmodels.png)

        urls.py

        ![urls.py](documentation/testing/pep8/profiles/pep8profilesurls.png)

        views.py

        ![views.py](documentation/testing/pep8/profiles/pep8profilesviews.png)

      - teachers app

        urls.py
        
        ![urls.py](documentation/testing/pep8/teachers/pep8teachersurls.png)

        views.py

        ![views.py](documentation/testing/pep8/teachers/pep8teachersviews.png)


    </details>

- HTML

  - No errors were returned when passing through the official [W3C validator](https://validator.w3.org/)

    <details>
    <summary>Click to expand to view the HTML testing</summary>

    - Bag

        Propper authentication needed to access this page

        [bag W3C validator]()

        ![bag](documentation/testing/html/bag/htmlbag.png)

    - Checkout

        Propper authentication needed to access these pages

        - checkout.html
        - checkoutsuccess.html

        [checkout W3C validator]()

        ![checkout](documentation/testing/html/checkout/htmlcheckout.png)

        [checkout success W3C validator]()

        ![checkout success](documentation/testing/html/checkout/htmlcheckoutsuccess.png)

    - Contact

        [contact W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Flanguageschoolproject.herokuapp.com%2Fcontact%2F)

        ![contact](documentation/testing/html/contact/htmlcontact.png)

    - Courseinfo

        [courseinfo W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Flanguageschoolproject.herokuapp.com%2Fcourseinfo%2F)

        ![courseinfo](documentation/testing/html/courseinfo/htmlcourseinfo.png)

    - Courses



        [course detail W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Flanguageschoolproject.herokuapp.com%2Fcourses%2F29%2F)

        ![course detail](documentation/testing/html/courses/htmlcoursedetail.png)

        [courses W3C validator]()

        ![courses course](documentation/testing/html/courses/htmlcourses.png)

        

        Propper authentication needed to access these pages:

        - add_course.html
        - delete_course.html
        - edit_course.html

        [add course W3C validator]()

        ![add course](documentation/testing/html/courses/htmladdcourse.png)

        [delete course W3C validator]()

        ![delete course](documentation/testing/html/courses/htmldeletecourse.png)

        [edit course W3C validator]()

        ![edit course](documentation/testing/html/courses/htmleditcourse.png)
    
    - Home

        [home W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Flanguageschoolproject.herokuapp.com%2F)

        ![homepage](documentation/testing/html/home/htmlhome.png)

    - Profiles

        Propper authentication needed to access this page

        - profile.html

        [profiles W3C validator]()

        ![profile](documentation/testing/html/profiles/htmlprofile.png)

    - Teachers

        [teachers W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Flanguageschoolproject.herokuapp.com%2Fteachers%2F)

        ![teachers](documentation/testing/html/teachers/htmlteachers.png)

    - Account

        login.html

        [login W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Flanguageschoolproject.herokuapp.com%2Faccounts%2Flogin%2F)

        ![login](documentation/testing/html/account/htmllogin.png)


        signup.html

        [signup W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Flanguageschoolproject.herokuapp.com%2Faccounts%2Fsignup%2F)

        ![signup](documentation/testing/html/account/htmlsignup.png)


        Propper authentication needed to access this page
        - logout.html

        [logout W3C validator]()  

        ![logout](documentation/testing/html/account/htmllogout.png)


    </details>

- CSS
  - No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Flanguageschoolproject.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)

      ![CSS validation](documentation/testing/css/cssvalidation.png)

- Accessibility
  - The page passes the accessibility test using lighthouse in devtools

    ![Lighthouse](documentation/screenshots/lighthouse.png)

## Bugs
### Fixed Bugs

The following bugs were tracked and fixed using the GitHub Issues tracker with the label of "bug".

[GitHub Issues Tracker Closed Issues](https://github.com/JulianeGampe/language-school/issues?q=is%3Aissue+is%3Aclosed)

- **Calculating shopping bag total not working** - [#1](https://github.com/JulianeGampe/language-school/issues/28)
- **NoReverseMatch at /courses/edit/10** - [#2](https://github.com/JulianeGampe/language-school/issues/29)
- **Navbar Dropdown not opening** - [#3](https://github.com/JulianeGampe/language-school/issues/30)
- **Allauth templates cannot be changed** - [#4](https://github.com/JulianeGampe/language-school/issues/32)

### Remaining Bugs

- No remaining bugs that I am aware of.

---

Return to the [README](README.md) file
