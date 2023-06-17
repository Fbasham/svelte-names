<script>
  import { onMount } from "svelte";
  let data = [];

  onMount(async () => {
    let res = await fetch("http://127.0.0.1:8000");
    data = (await res.json()).data;
  });
</script>

{#each data as d}
  <div>
    {d.name}
    {d.gender}
    {d.freq}
  </div>
{/each}
