from pyscript import document

def candidate_checker(e):
    club_members = ["River Datiles", "Rain Datiles", "Gilliah Tabaldo", "Milli Meneses", "Aaron De Guzman", "Ranee De Guzman", "Lexie Uaje", "Antonio Salonga", "Lan Aguilar", "Ange Del Rosario", "Rafa Dawinan"]
    f_name = document.getElementById("f_name").value
    l_name = document.getElementById("l_name").value
    candidate = f_name + ' ' + l_name
    member_checker = candidate in club_members

    messages = (f'Sorry, {candidate}, your name is not on the list.',
                f'Congratulations, {candidate}, you are a member of the Marching Band!')

    # False selects the rejection message; True selects the approval message.
    document.getElementById('result').innerHTML = messages[member_checker]