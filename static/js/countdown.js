 // Set the countdown date and time (replace with your own)
        var countdownDate = new Date("2024-02-20T23:59:59");

        // Update the countdown every 1 second
        var countdownTimer = setInterval(function() {
            // Get the current date and time
            var now = new Date().getTime();

            // Calculate the remaining time
            var timeDifference = countdownDate - now;

            // Calculate days, hours, minutes, and seconds
            var days = Math.floor(timeDifference / (1000 * 60 * 60 * 24));
            var hours = Math.floor((timeDifference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            var minutes = Math.floor((timeDifference % (1000 * 60 * 60)) / (1000 * 60));
            var seconds = Math.floor((timeDifference % (1000 * 60)) / 1000);

            // Update the countdown display with animation for changing numbers
            updateCountdown("days", days);
            updateCountdown("hours", hours);
            updateCountdown("minutes", minutes);
            updateCountdown("seconds", seconds);

            // If the countdown is finished, display a message
            if (timeDifference < 0) {
                clearInterval(countdownTimer);
                document.getElementById("countdown").innerHTML = "<h2>Акция</h2>";
            }
        }, 1000);

        function updateCountdown(id, value) {
            var element = document.getElementById(id);
            var currentVal = parseInt(element.innerText);

            // Add or remove the 'animate' class based on whether the value has changed
            if (currentVal !== value) {
                element.classList.add("animate");
            } else {
                element.classList.remove("animate");
            }

            // Update the value
            element.innerText = value;
        }
