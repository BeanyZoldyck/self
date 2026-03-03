<script>
	import { resolve } from '$app/paths';
	import Link from './link.svelte';
	let things = ['about', 'blog', 'contact', 'projects'];
</script>

<section class="py-20">
	<h1 class="mb-6 text-5xl font-bold text-purple-300 md:text-6xl">
		Hi, I'm <span class="text-purple-200">chuka</span>
	</h1>
	<p class="mb-8 text-xl text-purple-400 md:text-2xl">I do things sometimes</p>
	<div class="flex gap-4">
		{#each things.sort(() => Math.random() - 0.5) as thing}
			<Link {thing}></Link>
		{/each}
	</div>
</section>
