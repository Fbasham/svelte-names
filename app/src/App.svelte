<script>
  import FaRegHeart from "svelte-icons/fa/FaRegHeart.svelte";
  import FaLock from "svelte-icons/fa/FaLock.svelte";
  import FaLockOpen from "svelte-icons/fa/FaLockOpen.svelte";
  import FaTrash from "svelte-icons/fa/FaTrash.svelte";
  import { onMount } from "svelte";

  let data = [];
  let numNames = 0;
  let names = [];
  let favourites = [];

  onMount(async () => {
    let res = await fetch("http://127.0.0.1:8000");
    data = (await res.json()).data;
    if (localStorage.getItem("favourite-names")) {
      favourites = JSON.parse(localStorage.getItem("favourite-names"));
    }
  });

  function getRandomName() {
    return data[(Math.random() * data.length) | 0];
  }

  function handleChange(e) {
    let n = e.target.value;
    if (n == numNames) return;
    else if (n < numNames) names = names.slice(0, -1);
    else names = [...names, { name: "", locked: false }];
    numNames = n;
  }

  function addToFavourites(name) {
    favourites = [...new Set([...favourites, name])];
    localStorage.setItem("favourite-names", JSON.stringify(favourites));
  }

  function removeFromFavourites(name) {
    favourites = favourites.filter((e) => e !== name);
    localStorage.setItem("favourite-names", JSON.stringify(favourites));
  }
</script>

<h1>Svelte Names</h1>

<main>
  <section>
    <h2>Favourites</h2>
    <ul>
      {#each favourites as name}
        <li>
          <span>{name}</span><button
            on:click={() => removeFromFavourites(name)}
            class="icon-btn"><FaTrash /></button
          >
        </li>
      {/each}
    </ul>
  </section>
  <section>
    <h2>Find names</h2>
    <input
      type="number"
      min="1"
      max="5"
      on:change|preventDefault={handleChange}
    />
    <button
      on:click={() =>
        (names = names.map((o) =>
          o.locked ? o : { ...o, ...getRandomName() }
        ))}>random</button
    >
    {#each names as o, i}
      <div class="name-group">
        <p>{o.name || "[ new name ]"}</p>
        <button
          on:click={() => (names[i] = { ...names[i], locked: !o.locked })}
          disabled={!o.name}
          class="icon-btn"
        >
          {#if o.locked}
            <FaLock />
          {:else}
            <FaLockOpen />
          {/if}
        </button>
        <button
          on:click={() => addToFavourites(o.name)}
          disabled={!o.name}
          class="icon-btn red"><FaRegHeart /></button
        >
      </div>
    {/each}
  </section>
</main>

<style>
  main {
    display: grid;
    grid-template-columns: 1fr 1fr;
  }
  .icon-btn {
    cursor: pointer;
    border: none;
    height: 1.4rem;
    width: 1.4rem;
    background-color: transparent;
  }
  .icon-btn:nth-of-type(1) {
    margin-left: 0.5rem;
  }
  .icon-btn:hover {
    color: #333;
  }
  .red {
    color: red;
  }
  ul {
    display: flex;
    flex-direction: column;
    padding: 0;
  }
  li {
    display: flex;
  }
  .name-group {
    display: flex;
    align-items: center;
  }
</style>
