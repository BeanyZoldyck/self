<script lang="ts">
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
		<div class="border-l-2 border-purple-700 pl-6">
			<p class="text-lg text-purple-400">{header}</p>
		</div>

		<p class="text-white">{articles[`${link}`]}</p>
	</div>
</section>
