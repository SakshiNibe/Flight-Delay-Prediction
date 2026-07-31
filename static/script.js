// Flight Delay Prediction System

document.addEventListener("DOMContentLoaded", function () {

    const form = document.querySelector("form");

    form.addEventListener("submit", function (e) {

        const day = parseInt(
            document.querySelector('input[name="day"]').value
        );

        const month = parseInt(
            document.querySelector('input[name="month"]').value
        );

        const departureTime =
            document
            .querySelector('input[name="departure_time"]')
            .value
            .trim();


        // Validate Day

        if (isNaN(day) || day < 1 || day > 31) {

            alert("Please enter a valid day (1-31).");

            e.preventDefault();

            return;
        }


        // Validate Month

        if (isNaN(month) || month < 1 || month > 12) {

            alert("Please enter a valid month (1-12).");

            e.preventDefault();

            return;
        }


        // Validate Departure Time

        if (!/^\d{4}$/.test(departureTime)) {

            alert(
                "Enter departure time in HHMM format. Example: 1430"
            );

            e.preventDefault();

            return;
        }


        // Extract hour and minute

        const hour =
            parseInt(departureTime.substring(0, 2));

        const minute =
            parseInt(departureTime.substring(2, 4));


        // Validate time

        if (
            hour < 0 ||
            hour > 23 ||
            minute < 0 ||
            minute > 59
        ) {

            alert("Please enter a valid departure time.");

            e.preventDefault();

            return;
        }

    });

});