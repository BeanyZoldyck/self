<script lang="ts">
	import { resolve } from '$app/paths';
	export let title;
	export let header;
	export let link;
	import site from './site.txt?raw';
	const articles: any = { site };
	console.log(articles[`${link}`]);
</script>

<section class="py-20">
	<h1 class="mb-8 text-4xl font-bold text-purple-300">{title}</h1>

	<div class="space-y-6">
		<div class="border-l-2 border-purple-800 pl-6">
			<p class="text-lg text-purple-600">{header}</p>
		</div>
		{#each articles[`${link}`].split('\\n') as paragraph}
			<p class="text-white">{paragraph}</p>
		{/each}
	</div>
	<div class="mt-15 border-l-2 border-purple-900 pl-6">
		<a class="text-lg text-purple-800" href={resolve('/blog')}> ← back</a>
	</div>
</section>
