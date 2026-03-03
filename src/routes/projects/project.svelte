<script>
	export let title;
	export let desc;
	export let link;
</script>

<div class="border border-purple-900 p-6 transition-colors hover:border-purple-700">
	<h2 class="mb-2 text-2xl font-bold text-purple-200">{title}</h2>
	<p class="mb-4 text-purple-400">
		{desc}
	</p>
	<a href={link} target="_blank" class="text-mauve-700">{title}</a>
</div>
