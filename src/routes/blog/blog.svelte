<script>
	import { goto } from '$app/navigation';
	import { resolve } from '$app/paths';

	export let title;
	export let desc;
	export let link;
</script>

<a
	href={resolve('/blog/' + link)}
	class="block border border-purple-900 p-6 transition-colors hover:border-purple-700"
>
	<h2 class="mb-2 text-2xl font-bold text-purple-200">{title}</h2>
	<p class="mb-2 text-purple-400">
		{desc}
	</p>
	<span class="text-purple-700 hover:border-purple-500">read</span>
</a>
