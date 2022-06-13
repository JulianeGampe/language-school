# Learn German Online

Learn German Online is the website of a fictitious online language school. It offers online language classes for German as a foreign language and is targeted towards users who want to learn German in online classes. The students can create an account and purchase courses for different language levels and different formats (i.e. Standard, Business). The purchased courses will be saved and visible in their online profile. There are some information pages as well, on which the students can read more about the course structure and the teachers and where they can fill in a contact form if they have additional questions.

For the admin there is also the possibility to add new courses directly from the frontend. This page, along with the possibility to edit or delete existing courses, becomes accessible after login with admin credentials.

![Responsive Mockup](documentation/screenshots/amiresponsive.png)

## User Stories

### Student
#### Viewing and Navigation
1.	As a student I can see the home page so that I get an overview of what I can learn.
2.	As a student I can see and browse all available courses so that I can make a choice on which one to book.
3.	As a student I can see the details of an individual course so that I can see all necessary information including a course description.
4.	As a student I can see general information about the offered courses and language levels so that I can decide better which course is the right one for me.
5.	As a student I can see information about the teachers so that I can reassure myself about the quality of the offered classes.
6.	As a student I can see contact details of the language school so that I can get in touch in case I have additional questions.
7.	As a student I can see a link to the schools Facebook page so that I can connect with them via social media.
8.	As a student I can sign up for the schools newsletter so that I can receive newsletters with up-to-date information.

#### User account
9.	As a student I can register for an account so that I am able to view my profile. 
10.	As a student I will receive a confirmation email after registering so that I know that my account registration was successful. 
11.	As a student I can login and logout of my account so that I can access my personal information.
12.	As a student I have a personalized user profile so that I can view the courses that I have booked.
13.	As a student I can recover my account password so that I can access my account in case I forgot my password.

#### Sorting and Searching
14.	As a student I can sort the list of all available courses by level so that I can see courses matching my current language level.
15.	As a student I can sort the list of all available courses by course format so that I can quickly choose courses from my preferred course format.
16.	As a student I can sort the list of all available courses by the start date of the course so that I can choose a course that starts on a suitable date.
17.	As a student I can sort the list of all available courses by the weekday on which the course will take place so that I can find a course that fits my schedule.

18.	As a student I can search for a course by level or course format to find a specific course that I want to book.
19.	As a student I can easily see what I have searched for so that I can quickly decide if my desired course is available.


#### Purchase and Checkout
20.	As a student I can see the course(s) that I have in my shopping bag so that I can see which course(s) I am about to purchase.
21.	As a student I can remove a chosen course from my shopping bag so that I can make changes to my purchase before I checkout.
22.	As a student I can easily enter my payment information so that I can check out quickly. 
23.	As a student I can view an order confirmation after checkout so that I can verify I have booked the correct course(s).
24.	As a student I will receive an email confirmation after purchase so that I can keep the confirmation of my course(s) for my records.

### Admin
25.	As an admin I can add new courses to the website so that I can immediately offer new courses once they are organized with the teachers.
26.	As an admin I can edit/update a course so that I can change the status or correct any mistakes.
27.	As an admin I can delete a course so that I can remove a course I have accidentally created.

### Student + Admin
28. As a student/admin I can see messages on the screen so that I know the result of my input.

## UX
### Color Scheme

As a first step the color extractor from [Adobe Color](https://color.adobe.com/create/image) has been used to extract colors from the home page image and the image in the navbar brand.

![Color Tool Home Page](documentation/screenshots/extractcolor.png)
![Color Tool Navbar](documentation/screenshots/extractcolortwo.png)

The light blue color #E4EAF2 from the homepage image has been used as the background color on all pages. The darker blue color #B8C6D9 from the homepage image has been used as the background color for the navbar and footer.

The almost black color #262626 from the navbar image has been used as a background color for the buttons on the website. The dark red color #8C0303 has been used as the font color for the disclaimer in the footer and on the checkout page as well as for the warning on the delete course page.

Black #000 was used as font color throughout the page as it contrasts well with the chosen background colors. White #FFF was used as the background color for the buttons as this contrasts well with the chosen button colors.

The contrasts of all colors have been checked in a contrast checker. The contrast testing can be found in  the [TESTING.md](TESTING.md) file. 

### Typography 

Google Fonts has been used to find the font, that is displayed on the website. [Source Serif Pro](https://fonts.google.com/specimen/Source+Serif+Pro#standard-styles) is a serif typeface. As described on Google Fonts the font is designed for a digital environment with simplified letter shapes that are highly readable. It was used for the website to make the content easy to read and navigate for potential and current students.

To provide visual cues icons from [Font Awesome](https://fontawesome.com/) have been used for the social media icon in the footer as well as on the buttons and the exlamation mark of the checkout page and the search icon for the search bar on the courses page.

### Wireframes

Wireframes created with Balsamiq were used to plan the layout of the website.

![Wireframe Homepage](documentation/wireframes/home.png)
![Wireframe Homepage Mobile](documentation/wireframes/homemobile.png)
![Wireframe Our Courses](documentation/wireframes/ourcourses.png)
![Wireframe Our Courses Mobile](documentation/wireframes/ourcoursesmobile.png)
![Wireframe Course Detail](documentation/wireframes/coursedetail.png)
![Wireframe Course Detail Mobile](documentation/wireframes/coursedetailmobile.png)
![Wireframe Course Information](documentation/wireframes/courseinformation.png)
![Wireframe Course Information Mobile](documentation/wireframes/courseinformationmobile.png)
![Wireframe Our Teachers](documentation/wireframes/ourteachers.png)
![Wireframe Our Teachers Mobile](documentation/wireframes/ourteachersmobile.png)
![Wireframe Contact](documentation/wireframes/contact.png)
![Wireframe Contact Mobile](documentation/wireframes/contactmobile.png)
![Wireframe Shopping Bag](documentation/wireframes/shoppingbag.png)
![Wireframe Shopping Bag Mobile](documentation/wireframes/shoppingbagmobile.png)

### Flowchart

A flowchart created with Power Point was used to plan the models for the website.

![Flowchart](documentation/wireframes/modelflowchart.png)
![Flowchart Two](documentation/wireframes/modelflowcharttwo.png)

## Features 

### Existing Features

- __Navigation Bar__

    - Featured on all pages the navigation bar includes links to the Homepage, Our Courses, About Us and My Profile. Our Courses has a dropdown menu with sorting options. About Us has a dropdown menu linking to Course Information, Our Teachers and Contact. When not logged in My Profile links to Login and Sign Up. When logged in the My Profile page is accessible and Logout is visible, while Sign Up and Login disappear. When the admin is logged in there is a link to the Add Course page as well. Additionally, when logged in the menu link to the Shopping Bag will appear, displaying the current total in the shopping bag as well.
    - The navigation bar is fully responsive and identical on all pages to offer easy navigation.
    - It allows the user to easily navigate between the different pages across all devices, without having to use the “back” or “forward” buttons.
    - On small screen sizes the navbar will collapse into a toggler icon to keep the page well arranged.

![Navigation Bar](documentation/screenshots/navbar.png)
![Navigation Bar Toggler](documentation/screenshots/navbartoggler.png)

- __Home Page__

  - The Home Page will allow the user to see the aim and purpose of the website.
  - It includes links to the courses page as well as to the Course Structure, Teachers and Contact Page.
  - There is also a form to sign up for the newsletter.

![Home Page](documentation/screenshots/homepageone.png)
![Home Page](documentation/screenshots/homepagetwo.png)

- __Our Courses Page__

    - The Our Courses Page allows the user to see all offered courses.
    - It includes a dropdown menu to sort the courses as well as a searchbar to search for courses. This allows the students to easily find a suitable course for them.

![Our Courses](documentation/screenshots/courses.png)

- __Course Detail Page__

    - On the Course Detail Page the student can find all course information including the course description.
    - There is a button to add the course to the shopping bag, if there are still places left for the course. Otherwise there will be a message, that the course is already booked out. The course can only be added once to the bag. Once the course is in the bag, that message will be displayed. It can only be added once, as the name on the booking has to match the name of the student participating in the course.
    - If the student has already booked the course, a message with a link to the confirmation will be displayed.
    - When logged in as admin there will also be the buttons to edit or delete the course.

- Course Detail Admin:
![Course Detail Admin](documentation/screenshots/coursedetailadmin.png)
- Course Detail Student:
![Course Detail Student](documentation/screenshots/coursedetailstudent.png)

- __Course Information Page__

    - The course information page offers an explanation and overview of the language levels and the offered course formats.
    - This will allow especially new students to get addiotional information regarding the course structure and they can decide for the most suitable course for them.

![Course Information](documentation/screenshots/courseinformation.png)

- __Our Teachers Page__

    - The Our Teachers page offers a short introduction and information about the teachers of Learn German Online.
    - This will allow the students to assure themselves of the qualifacations of the schools teachers.

![Our Teachers](documentation/screenshots/teachers.png)

- __Contact Page__

    - On the Contact Page the students can find different options on how to contact the language school.
    - It offers a Contact Form that can be filled in with individual questions as well.
    - This allows students who have any doubts to address their questions directly on the website.

![Our Teachers](documentation/screenshots/contact.png)

- __Sign Up Page__

    - The Sign Up Page allows the students to create an account.
    - It requires a username, password and email address.
    - A confirmation email will be sent to the student with a link to verify the email address.

![Sign Up](documentation/screenshots/signup.png)

- __Login Page__

    - The Login Page allows students, who already created an account, to login with their username and password.

![Login](documentation/screenshots/signin.png)

- __Logout Page__

    - The Logout Page allows the user to logout.

![Logout](documentation/screenshots/signout.png)

- __Shopping Bag Page__

    - Logged in students can add courses to their shopping bag.
    - The shopping bag page displays the chosen courses or, if no courses a chosen yet, a link to the courses page.
    - The courses in the shopping bag can also be removed from the bag by click on the respective button.
    - When the students want to purchase the chosen course(s) they can click on the Secure Checkout button, which also displays the total order amount.

![Shopping Bag](documentation/screenshots/shoppingbag.png)

- __Secure Checkout Page__

    - This page allows the students to complete their purchase by entering their information and credit card details.
    - If the student has their address already saved on their profile, this data will be prefilled into the checkout form.
    - Respectively the student can also check the box to save the entered information to the profile.

![Checkout Top Page](documentation/screenshots/checkoutone.png)
![Checkout Bottom Page](documentation/screenshots/checkouttwo.png)


- __Checkout Success/Confirmation Page__

    - The Checkout Success Page will display an overview of the order.
    - It appears right after successfully making a purchase.
    - It can also be accessed later on from the booking history in the profile page.

![Checkout Confirmation](documentation/screenshots/checkoutconfirmation.png)

- __My Profile Page__

    - The profile page is visible when logged in.
    - The profile page allows the user to save or edit their address information. If they have already made a purchase with the option to save their information checked, this information will be prefilled here.
    - On the profile page the student can see their booked coures as well. For each booked course the student can also access the booking confirmation by clicking on the order number.

![Profile Page](documentation/screenshots/profile.png)

- __Add Course Page__

    - The add course page is visible to the admin only, when logged in.
    - It allows the admin to add a course directly from the frontend.

![Add Course Page](documentation/screenshots/addcourse.png)

- __Edit Course Page__

    - When logged in as admin the Edit Button will appear on the Course Detail Page of the chosen course.
    - The edit course page is visible to the admin only.
    - It allows the admin to edit a course directly from the frontend.

![Edit Course Page](documentation/screenshots/editcourse.png)

- __Delete Course Page__

    - When logged in as admin the Delete Button will appear on the Course Detail Page of the chosen course.
    - The delete course page is visible to the admin only.
    - It allows the admin to delete a course directly from the frontend.

![Delete Course Page](documentation/screenshots/deletecourse.png)

- __Footer__

    - The footer displays a link to the social media website of Learn German Online, so that the student can easily follow them there.
    - There is also a link to the privacy policy.

![Footer](documentation/screenshots/footer.png)

- __Messages__

    - Messages are displayed at the top of the screen to notify the student about the outcome of their actions (i.e. adding an item to the shopping bag, updating the profile).
    - The same applies to the admin. The admin will also be notified when the have added, edited or deleted a course.
    - This way the student/admin will know when they have changed content.

![Messages Example One](documentation/screenshots/messageone.png)
![Messages Example Two](documentation/screenshots/messagetwo.png)

### Features Left to Implement

- __Display Teacher for course & Course search by teacher__

    - Display which teacher is teaching the course and add the functionality to search for courses with specific teachers

- __Teacher Admin__

    - An admin page especially for the teachers, where they can see an overview of the courses they teach together with information about the attending students.
    - It could also contain the functionality to see the submitted contact forms on the frontend and mark them as replied, when a reply has been sent to the student.
    - Additionally the email addresses for the newsletter could be visible on the frontend for teachers who are in charge of creating the newsletter.

## Database Models

 - The courses, checkout, contact and homepage app require databases to store information. The following models have been build:
    - courses: Level, Format, Course
    - checkout: Order, OrderLineItem
    - contact: Contact
    - homepage: Newsletter

 __Level & Format__

![Level & Format Model](documentation/screenshots/levelformatmodel.png)

 __Course__

![Course Model](documentation/screenshots/coursemodel.png)

 __Order__

![Order Model Part 1](documentation/screenshots/ordermodelone.png)
![Order Model Part 2](documentation/screenshots/ordermodeltwo.png)

 __OrderLineItem__

![OrderLineItem](documentation/screenshots/orderlineitemmodel.png)

 __Contact__

![Contact](documentation/screenshots/contactmodel.png)

 __Newsletter__

![Newsletter](documentation/screenshots/newslettermodel.png)

## Technologies Used

- HTML 
    - was used to structure the website semantically and display it in the browser.
- [Bootstrap](https://getbootstrap.com/) 
    - CSS framework used to build responsive design.
- CSS 
    - was used for additional presentation and style of the website.
- JavaScript 
    - was used to make the website interactive.
- [Python](https://www.python.org/) 
    - was used as programming language to write the code.
- [Django](https://www.djangoproject.com/)
    - framework has been used to build the project and the apps.
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) 
    - is used to create the forms in the application.
- [TinyMCE](https://www.tiny.cloud/) 
    - is used as the text editor.
- [Gitpod](https://www.gitpod.io/) 
    - was used for the development of the website.
- [Github](https://github.com/) 
    - was used to store the code online.
- Git 
    - was used for version control.
- [The GitHub Projects Board](https://github.com/JulianeGampe/travel-blog/projects/1) 
    - was used to keep track of tasks that are still to do or in progress or see tasks that are already done.
- [The GitHub Issues tracker](https://github.com/JulianeGampe/travel-blog/issues) 
    - was used to keep track of bugs and add solutions.
- [Balsamiq](https://balsamiq.com/wireframes/) 
    - was used to create the wireframes.
- [Font Awesome](https://fontawesome.com/) 
    - was used for the icons.
- [Cloudinary](https://cloudinary.com/) 
    - is used to store and upload the images.
- [Heroku](https://www.heroku.com/home) 
    - is used to deploy the application
- [Google Fonts](https://fonts.google.com/)
    - was used for the website font
- [Adobe Color](https://color.adobe.com/create/image)
    - was used for extracting the colors from the homepage image and for color testing.


## Testing

Due to the length of testing, you can see all tests in the [TESTING.md](TESTING.md) file.

## Deployment

- The site was deployed to Heroku.
- Steps for deployment
  - Create a new Heroku app

  ![Create App](documentation/screenshots/createapp.png)
  ![Create App Step 2](documentation/screenshots/createappstep2.png)

  - Attach the database
      1. click on the _Resources_ tab
      2. in the add-ons bar search for Postgres and add it to the project
  
  ![Attach Database](documentation/screenshots/attachdatabase.png)

  - Set up the _Config Vars_ 
      1. DATABASE_URL is the connection to the Postgres database and is added to the project
      2. add the SECRET_KEY from the django project
      3. add the CLOUDINARY_URL
      4. add the TINYMCE_API key

  - Link the Heroku app to the repository in the _Deploy_ tab

  ![Connect to GitHub](documentation/screenshots/connecttogithub.png)
  ![Search Repository](documentation/screenshots/searchrepository.png)
  ![Connect to GitHub result](documentation/screenshots/connecttogithubresult.png)

  - Click on Deploy

  ![Deploy](documentation/screenshots/deploy.png)
  ![Deploy result](documentation/screenshots/deployresult.png)


The live link can be found here - https://

### Local Deployment

If you would like to make a local copy of this repository, you can clone it by typing the following command in your IDE terminal:
- `git clone https://github.com/JulianeGampe/language-school.git`

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/JulianeGampe/language-school)

You must install the required packages for this application, using the command:
- `pip3 install -r requirements.txt`

You must set the keys for your environment variables in env.py:
- os.environ["DATABASE_URL"] 
- os.environ["SECRET_KEY"]
- os.environ["CLOUDINARY_URL"]
- os.environ["TINYMCE_API"]

## Credits 

### Content

- This [YouTube Video](link) from .... have been used for help with ....
- This article from [Name](link) was used to ....

### Media 

- The following website was used to ...
- The image for ... has been taken from ....[Website](link)

### Acknowledgements

- I would like to thank ....




![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome JulianeGampe,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Gitpod and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **September 1, 2021**

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

------

## Release History

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**September 1 2021:** Remove `PGHOSTADDR` environment variable.

**July 19 2021:** Remove `font_fix` script now that the terminal font issue is fixed.

**July 2 2021:** Remove extensions that are not available in Open VSX.

**June 30 2021:** Combined the P4 and P5 templates into one file, added the uptime script. See the FAQ at the end of this file.

**June 10 2021:** Added: `font_fix` script and alias to fix the Terminal font issue

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Happy coding!
