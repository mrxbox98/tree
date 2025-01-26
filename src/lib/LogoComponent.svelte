<div class="container">
    <div class="image-container">
        <img src="./logo.png" />
    </div>
    <div class="text-container">
        YourPlantFriend
    </div>

</div>

<style>
    .container {
        position: absolute;
        width: 100%;
        color: black;
        display: flex; /* Make the child divs align in a row */
        align-items: center; /* Vertically align items within the row */
        gap: 10px; /* Add space between the two divs */
    }

    .image-container {
        height: 55px;
        width: 55px;
    }

    .image-container img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }

    .text-container {
        font-size: 25px;
        font-family:cursive;
        color: #8CC342; /* Optional: Set text color for contrast against the background */
    }
</style>
