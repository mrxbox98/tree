<script lang="ts">
    import { getAmazonPrices, getLatLong, getPlants, getZipCode } from "$lib/client";
    import { onMount } from "svelte";

    let zipCode = 0;

    let plant = []

    let priceData = [{}]

    onMount(async () => {
        let location = await getLatLong();

        zipCode = await getZipCode(location.lat, location.long);

        plant = await getPlants(zipCode);

        priceData = await getAmazonPrices(plant + " seeds");
    })
</script>

<div>
    Your zip code is : {zipCode}
</div>
<div class="flex">
    {#each plant as item}
        <div>
            <p>{item}</p>
        </div>
    {/each}
</div>
<div class="grid grid-cols-5">
    {#each priceData as item}
        <div>
            <p>{item.title}</p>
            <p>{item.price}</p>
        </div>
    {/each}
</div>
