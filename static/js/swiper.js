var prevScrollPos = window.pageYOffset || document.documentElement.scrollTop;
            var categoriesContainer = document.querySelector('.sticky-top');

            window.addEventListener('scroll', function() {
              var currentScrollPos = window.pageYOffset || document.documentElement.scrollTop;

              if (currentScrollPos > prevScrollPos && currentScrollPos > 510) {

                categoriesContainer.classList.remove('show');
                categoriesContainer.classList.add('hide');
              } else {

                categoriesContainer.classList.remove('hide');
                categoriesContainer.classList.add('show');
              }

              prevScrollPos = currentScrollPos;
            });