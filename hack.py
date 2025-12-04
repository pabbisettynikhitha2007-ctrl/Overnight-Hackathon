name: Overnight Hackathon Submission
description: Click Here to Submit Your Hackathon Project
title: "[Project]: "
labels: ["submission", "needreview"]
body:
  - type: markdown
    attributes:
      value: |
        Thanks for participating in the hackathon and creating your submission!
  - type: input
    id: name
    attributes:
      label: Name
      description: Enter your full name
      placeholder: Lipi Bujarbarua
    validations:
      required: true
  - type: input
    id: email
    attributes:
      label: Email Address
      description: Enter your email address
      placeholder: lipibujarbarua.cs25@rvce.edu.in
    validations:
      required: true
  - type: input
    id: team-emails
    attributes:
      label: Email Addresses of Team Members
      description: Enter the email addresses of you team members separated by commas (if you have any)
      placeholder: psnikhitha.cs25@rvce.edu.in, pochaomshivani.ci25@rvce.edu.in, kritikaagarwala.cs25@rvce.edu.in
    validations:
      required: false
  - type: textarea
    id: description
    attributes:
      label: Project Description
      description: What have you built during the hackathon?
      placeholder: The project I created is a web application which helps the students to understand the topics in their regional languages.
    validations:
      required: true
  - type: textarea
    id: inspiration
    attributes:
      label: Key Features
      description: describe the key features of your project which makes it unique from the solutions that already exist in the market
      placeholder: It not only translates the topics given , but also gives the basic understanding required for the students 
    validations:
      required: true
  - type: textarea
    id: tech-stack
    attributes:
      label: Tech Stack
      description: How have you built this project? Mention the technologies/methods/platforms you used to build your project
      placeholder: The technologies I used...
    validations:
      required: true
  - type: dropdown
    id: problem-statement
    attributes:
      label: Problem Statement
      description: Select the specific Problem Statement for your submission from the list below
      placeholder: "EdTech: 9. Vernacular STEM Learning Gap Analysis"
    validations:
      required: true 

    validations:
      required: true
  - type: input
    id: project-link
    attributes:
      label: Project Repo
      description: Share a public repo link of your project
      placeholder: https://github.com/github-id/project-repo
    validations:
      required: true
  - type: input
    id: ppt-link
    attributes:
      label: Presentation (PPT) Link
      description: Share a publicly visible presentation (PPT) link of your project
      placeholder: https://docs.google.com/presentation/d/your-presentation-id
    validations:
      required: true
  - type: input
    id: demo-link
    attributes:
      label: Demo Video/Photos
      description: Share a publicly visible demo video/photos link of your project
      placeholder: https://www.youtube.com/watch?v=9IBaX1avYWc
    validations:
      required: false
  - type: textarea
    id: anything-else
    attributes:
      label: Anything Else?
      description: Any other feedback, queries or information, you would like to share with us?
    validations:
      required: false
  - type: checkboxes
    id: terms
    attributes:
      label: Rules and Code of Conduct
      description: By submitting this issue, you agree to follow our Rules and Code of Conduct.
      options:
        - label: I agree to follow this hackathon's Rules and Code of Conduct
          required: true
