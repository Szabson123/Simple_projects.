document.addEventListener('DOMContentLoaded', function() {
  var numeryDiv = document.getElementById('numeryTelefonow');
  var emailDiv = document.getElementById('emails');
  var socialDiv = document.getElementById('socials');
  var links = document.querySelectorAll('.nav li');

  // Ustawienie początkowego wyświetlania sekcji
  numeryDiv.style.display = 'block';
  emailDiv.style.display = 'none';
  socialDiv.style.display = 'none';

  // Funkcja do zmiany aktywnego linku i wyświetlania odpowiedniej sekcji
  function setActiveLink(clickedLink, divToShow) {
    links.forEach(link => {
      link.classList.remove('active'); // Usuwanie klasy 'active' ze wszystkich linków
    });
    clickedLink.classList.add('active'); // Dodawanie klasy 'active' do klikniętego linku

    // Ukrywanie wszystkich sekcji
    numeryDiv.style.display = 'none';
    emailDiv.style.display = 'none';
    socialDiv.style.display = 'none';

    // Pokazywanie wybranej sekcji
    divToShow.style.display = 'block';
  }

  // Dodawanie event listenerów do linków
  document.getElementById('telefonLink').addEventListener('click', function() {
    setActiveLink(this, numeryDiv); // 'this' odnosi się do klikniętego elementu
  });

  document.getElementById('emailsLinks').addEventListener('click', function() {
    setActiveLink(this, emailDiv);
  });

  document.getElementById('socialLinks').addEventListener('click', function() {
    setActiveLink(this, socialDiv);
  });
});
