<script lang="ts">
    import { DATA, getAmazonPrices } from "$lib/client";

    export let flower = "";

    let mainel: HTMLElement;

    let info: any = undefined

    let loading = false;

    async function onHover() {
        loading = true

        //let amazonPrices = await getAmazonPrices(mainel.textContent+" seeds");

        //console.log(amazonPrices);

        //info = amazonPrices.find((el: {
        //    title: string;
        //}) => el.title.toLowerCase().includes("seed") || el.title.toLowerCase().includes("plant"));

        console.log(info);

        if(info==undefined) {
            let f = DATA.find((el) => (el.name.toLowerCase()+"s").includes(mainel.textContent.toLowerCase().split(",")[0]))

            info = {
                title: f?.name,
                link: f?.url,
                img: f?.img,
            }
        }

        box.style.top = `${mainel.getBoundingClientRect().top + mainel.getBoundingClientRect().height}px`;
        box.style.left = `${mainel.getBoundingClientRect().left}px`;
        box.style.display = "block";

        loading = false
    }

    function leave() {
        box.style.display = "none";
    }

    function show() {
        box.style.display = "block";
    }

    let box: HTMLElement;
</script>

<code
    bind:this={mainel}
    class={loading ? "cursor-wait" : ""}
    onmouseover={onHover} onmouseleave={leave}><b><i>{flower}</i></b></code
>

<div
    bind:this={box}
    onmouseenter={show}
    onmouseleave={leave}
    class="text-black w-[200px] absolute hidden p-3 bg-white rounded-lg shadow-lg shadow-gray-500/50"
>
    {#if info}
        <img src={info.img} alt="" class="rounded-lg" />
        <a href={info.link} target="_blank" class="hover:underline"
            >{info.title}</a
        >
        <p class="font-semibold text-right">{info.price}</p>
    {/if}
</div>
