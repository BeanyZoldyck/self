<script>
	export let title;
	export let desc;
	export let link;
	export let info = '';
</script>

<div class="border border-purple-900 p-6 transition-colors hover:border-purple-700">
	<h2 class="mb-2 text-2xl font-bold text-purple-200">{title}</h2>
	<p class="mb-2 text-purple-400">
		{desc}
	</p>
	<p class="mb-1 text-xs text-mauve-500">{info}</p>
	<a href={link} target="_blank" class="text-purple-700">{title}</a>
</div>
