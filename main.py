from pyscript import display, document

def calculateGWA(e):
    subjects = ["Filipino", "English", "Social Studies", "Math", "Science", "ICT"] #  list w subjects
    units = (3, 5, 3, 5, 5, 2) #  tuple w units

    fname= document.getElementById('student-fname').value
    lname= document.getElementById('student-lname').value
    section= document.getElementById('section').value
    info = fname + " " + lname + " - " + section
    filipino = document.getElementById("filipino").value
    english = document.getElementById("english").value
    ss = document.getElementById("social-studies").value
    science = document.getElementById("science").value
    math = document.getElementById("math").value
    ict = document.getElementById("ict").value

    document.getElementById("diva2").style.display = "block"
    document.getElementById("diva3").style.display = "block"

    if (fname == "" or lname == "" or section == "" or filipino == "" or 
        english == "" or ss == "" or science == "" or math == "" or ict == ""):
        display("Please complete all information.", target="diva3", append=False)
        return
    gwa = round((float(filipino) + float(english) + float(ss) + float(science) + float(math) + float(ict)) / 6, 2)
    
    summary = (
        f"Filipino: {filipino}\n"
        f"English: {english}\n"
        f"Social Studies: {ss}\n"
        f"Math: {math}\n"
        f"Science: {science}\n"
        f"ICT: {ict}\n"
    )

    display(info, target="diva2", append=False)
    display(summary, target="diva2")
    display(f"General Weighted Average: {gwa}", target="diva2", append=True)
