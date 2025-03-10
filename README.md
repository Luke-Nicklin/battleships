## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

# Battleships

Battleships is an interactive command line game that allows users to select a difficulty level between 'Easy' and 'Hard' and select coordinates in the form of rows and columns to sink the computer's ships. The game shows the user's boards with the placement of their ships and the computer's board where the ships are hidden. It notifies the user of a hit with an 'X' and a miss with an 'O'. The winner is determined when they sink all their opponent's ships first.

![Responsive Mockup](media/)

## Features 

The Battleships game includes the following features:

- User can select the difficulty of the game. 'Easy' creates a 5x5 board. 'Hard' creates a 9x9 board.
- User board and computer board.
- Radnom ship placement.
- Marking the board with 'X' for a hit and 'O' for a miss.
- Number of hits the user and computer has made.

### Existing Features

__Select difficulty__

  - When starting the game, the user is asked to select the difficulty between 'Easy' and 'Hard.
  - If they enter 'Easy', they will play using a 5x5 board.
  - If they enter 'Hard', they will play using a 9x9 board.

![Difficulty](media/)

__User and computer boards__

  - Once the user enters the difficulty, a board is created for the user and for the computer.

![Boards](media/)

__Random ship placement__

  - When the boards are created, the ships are randomly placed on both boards. The ships are visible on the user's board but hidden on the computer's board.
   
![Random ship placement](media/)

__Hits and misses__

  - To keep track of hits and misses, the game marks a hit with an 'X' and a miss with a 'O'. This is so the user can see what they've hit, what they've missed and coordinates they haven't selected yet. 

![Hits and misses](media/)

__Number of hits__ 

  - Each time the user or computer has a hit, the game shows the number of hits the user has made and the number of hits the computer has made. This allows the user to easily see who's winning and how many ships are left.

![Number of hits](media/)

### Features to implement in the future

- A version that allows the user to select where they want to place their ships
- The ability to include larger ships that span multiple coordinates

## Technologies

* Python
    * The entrie game was created using python.
    * Used to generate different sized boards based off of difficulty selected by the user.
    * Used to place ships randomly on each board.
    * Used to ask the user to select a row and a column to select a coordinate to fire at.
    * Used to display hits ('X') and misses ('O').
    * Used to display the number of user and computer hits.
    * Used to determine the winner when either the user or the computer has sunk all their opponent's ships. 
* Visual Studio Code
    * The game was developed using the Visual Studio Code text editor.
* GitHub
    * Source code is hosted on GitHub and delpoyed using Git Pages.
* Git 
    * Used to commit and push code during the development opf the Website 

## Testing

### Responsiveness

All pages were tested to ensure responsiveness on screen sizes from 320px and upwards as defined in [WCAG 2.2 Reflow criteria for responsive design](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html) on Chrome and safari browsers.

Steps to test:

1. Open browser and navigate to [RPSLS](/https://luke-nicklin.github.io/rpsls/)
2. Open the developer tools (right click and inspect)
3. Set to responsive and decrease width to 320px
4. Set the zoom to 50%
5. Click and drag the responsive window to maximum width

Expected:

Website is responsive on all screen sizes and no images are pixelated or stretched.

Actual:

Website behaved as expected.

### Accessibility

[Wave Accessibility](https://wave.webaim.org/) tool was used for final testing of the deployed website to check for any accessibility issues.

Testing checked to see if the following criteria were met:

- Color contrasts meet a minimum ratio as specified in [WCAG 2.2 Contrast Guidelines](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)
- Heading levels are not missed or skipped to ensure the importance of content is relayed correctly to the end user
- All content is contained within landmarks to ensure ease of use for assistive technology, allowing the user to navigate by page regions
- All non textual content had alternative text or titles so descriptions are read out to screen readers
- HTML page lang attribute has been set
- Aria properties have been implemented correctly
- WCAG 2.2 Coding best practices being followed

### Lighthouse Testing

__Home__

![Home](media/homepage-lighthouse.png)

__404 page__

![Meditation](media/404-lighthouse.png)

### Functional Testing

**Buttons**

Testing was performed to ensure all buttons resulted in the expected behaviour as per design. This was done by selecting each button on the home page and 404 page.

| Navigation Link | Page to Load     |
| --------------- | ---------------  |
| Home            | index.html       |
| 404             | 404.html         |

Buttons on all pages produced the expected behaviour.

Steps to test

1. Navigate to [RPSLS] (https://luke-nicklin.github.io/rpsls/)
2. Select "Rock" button
3. Select "Paper" button
2. Select "Scissors" button
3. Select "Lizard" button
2. Select "Spock" button

Expected behaviour

When the user selects a button the matching image will appear under the 'You' H2 and the computer's random move will generate the image that matches its move under the 'Computer' H2.

Actual:

Behaviour as expected

**Result**

Steps to test

1. Navigate to [RPSLS] (https://luke-nicklin.github.io/rpsls/)
2. Select "Rock" button
3. Select "Paper" button
2. Select "Scissors" button
3. Select "Lizard" button
2. Select "Spock" button

Expected behaviour

When the user selects a button, the result displays the outcome of each game. It will either say 'You win!', 'You lose!' or 'It's a tie!'

Actual:

Behaviour as expected

**Scoreboard**

Steps to test

1. Navigate to [RPSLS] (https://luke-nicklin.github.io/rpsls/)
2. Select "Rock" button
3. Select "Paper" button
2. Select "Scissors" button
3. Select "Lizard" button
2. Select "Spock" button

When the user selects a button, the scoreboard is updated with the result of each game. This is a running total of the results of all the games in the session.

Actual:

Behaviour as expected.

### Validator Testing 

- HTML
  - No errors were returned when passing the home page through the official [W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fluke-nicklin.github.io%2Frpsls%2F)
  - No errors were returned when passing the 404 page through the official [W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fluke-nicklin.github.io%2Frpsls%2F404)

- CSS
  - No errors were found when passing the home page through the official [W3C validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fluke-nicklin.github.io%2Frpsls%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)
  - No errors were returned when passing the 404 page through the official [W3C Validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fluke-nicklin.github.io%2Frpsls%2F404&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)

- JavaScript
  - No errors were found when passing the JavaScript code through the JSHint checker website ![JSHint](media/JShint%20-%20result-image.png) 

### Bugs

- Scoreboard

I encountered a bug with the scoreboard where it would reset for each game. Therefore, it did not keep a running track of the scores. I managed to fix this by moving the event listeneres and attaching them to the DOM variables. However this lead to an issue with the playGame function running twice every time a button was clicked.

I realised that I had an onclick="playGame('rock')" on each button within my HTML that was causing this issue. By removing this, the playGame function only ran once and the scoreboard went up in increments of one each time a game was played.

## Deployment

- The site was deployed to GitHub pages. The steps to deploy are as follows: 
  - In the GitHub repository, navigate to the Settings tab 
  - Select Pages in the 'Code and automation' section of the vertical navigation on the left side
  - Once the main branch has been selected and saved, the page will include the live URL at the top of the page with a visit site button.

The live link can be found here - https://luke-nicklin.github.io/rpsls/

### Version Control

The site was created using the Visual Studio Code editor and pushed to github to the remote repository 'rpsls'.

The following git commands were used throughout development to push code to the remote repo:

```git add <file>``` - This command was used to add the file(s) to the staging area before they are committed.

```git commit -m "commit message"``` - This command was used to commit changes to the local repository queue ready for the final step.

```git push``` - This command was used to push all committed code to the remote repository on github.

### Clone the Repository Code Locally

Navigate to the GitHub Repository you want to clone to use locally:

- Click on the code drop down button
- Click on HTTPS
- Copy the repository link to the clipboard
- Open your IDE of choice (git must be installed for the next steps)
- Type git clone copied-git-url into the IDE terminal

The project will now have been cloned on your local machine for use.


## Credits 

### Code

- CodeInstitute - JavaScript module helped me to implement certain aspects of the code such as the moves array, playGame function and else/if statements. It also showed me how to change the images when a button is selected using template literals in the example project video.
- StackOverflow - Helped me to troubleshoot issues I was having with JavaScrip throughout the project.
- SheCodes - Helped me work out how to use event listeners for the buttons.
- [Code with Ania Kubów](https://www.youtube.com/watch?v=RwFeg0cEZvQ) was used to help me better understand different ways to use JavaScript to make the game work.