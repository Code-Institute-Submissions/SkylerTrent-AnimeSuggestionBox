# AnimeSuggestionBox

## **Introduction**

This is the repository for **The Anime Suggestion Box** website.

The deployed site can be visited by clicking [**here**](https://anime-suggestion-box.herokuapp.com/).

The site code can be viewed in this [**GitHub Repository**](https://github.com/SkylerTrent/AnimeSuggestionBox).

My name is **Skyler Trent** and I designed and built this site using multiple technologies and frameworks. This site was designed and built for educational purposes to be submitted as my third major Milestone Project. The Anime Suggestion Box is a fully functional web app that allows users to add, edit, create, and view anime suggestions that other users have added.

## UX
### Project Goals:
The goal of this project was to create a web app that allowed users to perform CRUD operations while maintaining aesthetics and responsivness. 

* #### User Goals:
   * Access and view Anime added by other users.
   * Access and update information on Anime added by other users.
   * Access and delete information on Anime added by other users. 
   * Create new anime suggestion that accessible to others.
   * Responsive Web site.
   
### User Stories

As a user, I want to be able to view anime that other users have suggested. End-user goal: To easily view anime that others have suggested. Acceptance criteria: * product defines any initial functionality requirements they can think of.

As a user, I want the ability to update anime and its' information that has been submitted by other users. End-user goal: The ability to edit anime and its information provided by other users.

As a user, I want the ability to delete anime and its'  information that has been submitted by other users. End-user goal: The ability to delete anime and its information provided by other users.

As a user, I want the ability to add anime and its' information to the site thats viewable by others. End-user goal: The ability to add anime and its information the site thas viewable to othe users.

### Wireframes
I have provided an active link to my Wireframes.
Wireframes were used to assist in the creation of my site. They played a key role throughout its development. The Wireframes helped make the responsive design as well as the nav-bar that was used throughout the site on each of the pages. 

1. Wireframes:
   1. Index/Home Page https://wireframe.cc/CGX5ra
   1. Gallery Page https://wireframe.cc/TsrS12
   

## Features
 
### Existing Features
- Responsive design: Allows for the viewing of the site on small, medium, and large devices.
- Navbar
- Breadcrumbs
- Full CRUD Functionality.
- Database Searchbar

### Features Left to Implement
- A more interactive site as my knowledge increases.

 ## Technologies ##

### Languages ###

- [HTML5](https://developer.mozilla.org/en-US/docs/Web/HTML)
  - Used as the main markup language for the website content.
- [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS)
  - Used to style the individual webpages.
- [Javascript](https://developer.mozilla.org/en-US/docs/Web/javascript)
  - Used tomake pages interactive webpages.
- [Python](https://developer.mozilla.org/en-US/docs/Web/Python)
  - Used to communicate with the server backend.

### Libraries ###

- [Bootstrap](https://getbootstrap.com/)
  - Used to design a mobile-first responsive website layout.
- [jQuery](https://jquery.com/)
  - Loaded as part of the [Bootstrap CDN starter template](https://getbootstrap.com/docs/4.5/getting-started/introduction/#starter-template)
- [Popper](https://popper.js.org/)
  - Loaded as part of the [Bootstrap CDN starter template](https://getbootstrap.com/docs/4.5/getting-started/introduction/#starter-template)
- [Jinja2]//jinja.com)
    - The project uses **Jinja** Template language used to communicate with Flask. 
- [Flask]//flask.com)
    - The project uses **Flask** Template framework used to build the web app.
- [materialize]//https://materializecss.com/getting-started.html)
    - The project uses **materialize** for the grid layout, navbar and footer.
- [Bootstrap](https://Bootstrap.com)
    - The project uses **Bootstrap** to help me create the grid layout, header, Nav-Bar, and contact form. I used Bootstrap 4 (therefore I used Popper and jQuery that comes with it).
- [Google Fonts](https://Googlefonts.com)
    - The project uses **Google Fonts** I used 'Dosis' from Google Fonts, by only using one font it helped my site to appear more uniformed throughout.
- [code Institute](https://codeinstitute.com)
    - The project referenced what I have learned in **Mini projects from Code Institute**, I referenced three techniques. One was from the Whiskey Landing Page, as well as the picture rounding technique from the reviews. However I did make the code my own customizing the display positionings, colors, pictures, bootstrap, etc. The second technique that I referenced was from the Love Running Project. I used the location and times section with the Opaque overlay of the picture. However this code was made my own by customizing nearly aspect of it for it to work in my Bootstrap system. 
- [CodePen]//codepen.io/scanfcode/pen/MEZPNd)
    - The project uses **Code Pen** I used a footer template from this site that is used at the bottom of every page on the site. I made the code my own through customization. I made it so that it is responsive in Bootstrap, changed the background color, font color, content, CSS hover, and layout.  
 - [Font Awesome](https://Fontaesome.com)
    - The project uses **Font Awesome**. All of the social media icons in the footer are from Font Awesome).
 - [startBootstrap](https://www.youtube.com/watch?v=vUXdZuw_KP8)
    - The project uses **startBootstrap**I imported a the Freelancer theme from this website.). 
 - [W3 Schools]//https://www.w3schools.com/)
    - The project uses **W3 Schools** I used link hover effects and .card transparent overlays on the events page from this source.
    
 ## SEO ##

Search Engine Optimisation for the site was provided in three complementary ways:
 - HTML Sitemap links
 - XML sitemap file saved in the root directory
 - Google Search Console
 
#### HTML Sitemap links ####
- **Secondary** HTML links to each page in the website were added to the footer section of each site page to allow users an alternative means of navigating the site easily.

#### XML Sitemap file ####
- A sitemap.xml file was created to help search engines find, crawl and index the website more easily. It was created by using XML-Sitemaps.com and entering the URL for the deployed website and letting it automatically generate the required xml data for the whole site.
The file was then saved in the GitHub repository root directory.

- The following steps were used to generate the sitemap.xml file:
  1. Visit [XML-Sitemaps.com](https://www.xml-sitemaps.com/) and enter the URL of the website https://anime-suggestion-box.herokuapp.com/
  2. Click Start
  3. The site pages will automatically be scanned 
  4. Click View Sitemap Details
  5. Download the XML sitemap file
  6. Save the sitemap.xml file in the root directory of the GitHub repository

#### Google Search Console ####
- Google Search Console was used to assist with testing and indexing issues with the website and to see how the site performs in Google search results.

- The following steps were used to perform the indexing tests:
  1.  Visit [Google Search Console](https://www.google.com/webmasters/tools/home)
  2.  Click Add Property in the menu bar
  3.  Enter the website URL https://anime-suggestion-box.herokuapp.com/
  4.  Click Continue
  5.  Download the unique verification file created by Google
  6.  Save the [verification file](google717791873a15b1df.html) in the root directory of the GitHub repository
  7.  On Google Search Console, click Verify
  8.  Once the verification passes, the site is available in the Google Search COnsole dashboard.
  
## Version Control ##
**Version control** for this repository is managed within **GitHub** and **Gitpod** using separate [branches](https://github.com/simonjvardy/Aviation-Consultancy/branches)  used to work on specific aspects of the project.
The following describes the repository branch structure:
- **Master** - this is the default branch and the source for the repository deployment.
    - **Documentation** - this branch is used for updating the README.md and testing.md documentation only.
    - **Development** - this branch is used as the main working branch for the website development
    - Each individual **bug fixes** are raised within their own **separate branches** using the naming convention **\<GitHub Issue ID Number>-\<bug fix description>** e.g. branch name ***12-correct-navbar-links*** 

The following workflow steps are used to create and update branches within Gitpod and to push changes back to GitHub.

#### Gitpod Workspaces ####
1. Open **Gitpod** from **Github** using the Gitpod button. This needs to only be done **once** at the start of the project.
2. Start the Gitpod Workspace which opens an **online IDE editor** window.

#### Branches ####
3. For changes to be made to any **documentation files**, the git command `git checkout documentation` is used to checkout and switch to the **documentation branch**.
4. For changes to be made to **all other files**, the git command `git checkout development` is used to checkout and switch to the **development branch**.
5. To create a **new branch**, use the git command `git checkout -b <branch-name>` to **create and switch** to the new branch.

#### Working within a branch ####
6. **New** or **modified** files are **staged** using the `git add .` command
7. The changes are **committed** using `git commit -m "<commit message>"` command.
8. If the changes are in a newly created branch, the **committed** changes are **pushed** from Gitpod to GitHub using the `git push --set-upstream origin <branch-name>` command as there is currently no upstream branch in the remote repository.
9. For branches that have already been synchronised, the **committed** changes are **pushed** from Gitpod to GitHub using the `git push` command.

#### Merging branches in GitHub ####
10. Opening the repository in Github, a new **pull request** is created for the updated branch and assigned to the **Development project**.
11. The changes are **reviewed** to ensure there are **no conflicts** between the **updated branch** and the **Master branch**.
12. The changes are then **merged** into the **Master branch** and the merge request is **closed**. The **Project entry** is **automatically** moved to the **Done** card.

#### Update Gitpod with the latest GitHub commits ####
13. To update Gitpod with the **latest commits** From GitHub, the `git checkout master` command is used to checkout and switch to the master branch.
14. Use the `git pull` command to update the master branch and **reset the pointer**.
15. Now **switch** to the **other branches** in Gitpod using the `git checkout <branch-name>` command and use the `git merge origin/master` command to **update each branch in turn**.
16. Use the `git push` on **each branch** to update the relevant GiHub Branches to the **same commit** as the **Master branch**.
17. **Repeat steps 3 - 17 regularly** to ensure updates are **saved** and **correctly version controlled** in GitHub.

---
    
## Testing

1. Contact Form:
   1. Go to the "Contact" page
   1. Try to submit the empty form and verify that an error message about the required fields appears
   1. Try to submit the form with an invalid email address and verify that a relevant error message appears
   1. Try to submit the form with all inputs valid and verify that a success message appears.
   1. **Conclusion: By following these steps I was able to verify the 'Contact' page works successfully.**
   
1. Photo Gallery:
   1. Go to the 'Gallery' page
   1. Scroll halfway down the page until you reach 'Photo Gallery' section
   1. Hover the Photo Gallery Button-
   1. Select one of the 3 different photo gallery types
   1. **Conclusion: By following these steps I was able to verify all photo's in the gallerys were working**
   

1. Responsiveness:
   1. Navigate to 'Home' Page
   1. Open Chrome Dev tools by pressing the F12 key or by right-clicking the mouse on the page and selecting 'Inspect'
   1. Click the 'Responsive' drop-down option, located directly below the bookmark bar in Chrome
   1. Select a device 
   1. After selecting a device the page will mimic the screen size of the device chosen
   1. All of the elements will align to fit the current screen size chosen
   1. **Conclusion: By following these steps I was able to verify the Menu is available and displaying properly**
  
1. Links:
   1. Navigate to 'Home' page
   1. Click each link in the NavBar which takes the user to its respective page
   1. Scroll down the page to the next set of links and repeat step 1
   1. Scroll down to the footer and repeat step 1.
  
1. Code Validation Tools used:
   1. https://validator.w3.org/
   1. https://jigsaw.w3.org/css-validator/
   1. https://esprima.org/demo/validate used to test/validate Javascript.
   1. **Code passed all of the validation criteria**
    
 
## Deployment

To deploy this page to GitHub Pages from its GitHub repository, the following steps were taken:

1. From the menu items near the top of the page, select Settings.
1. Scroll down to the GitHub Pages section.
1. Under Source click the drop-down menu labeled None and select Master Branch.
1. On selecting Master Branch, the page is automatically refreshed, the website is now deployed.
1. Scroll back down to the GitHub Pages section to retrieve the link to the deployed website.



### How to run this program locally
To clone this project from GitHub:

Under the repository name, click "Clone or download".
In the Clone with HTTPs section, copy the clone URL for the repository.
In your local IDE open Git Bash.
Change the current working directory to the location where you want the cloned directory to be made.
Type git clone, and then paste the URL you copied in Step 3.
git clone https://github.com/SkylerTrent/up-in-smoke-bbq
Press Enter. Your local clone will be created.
Further reading and troubleshooting on cloning a repository from GitHub here.

## Credits

### Media
1. Photos:
  1. Google Images
  1. Eventbrite.com
