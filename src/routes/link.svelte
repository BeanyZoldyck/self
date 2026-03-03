<script>
	import { resolve } from '$app/paths';
	export let thing;
</script>

<a
	href={resolve('/about')}
	class="border border-purple-700 px-6 py-3 text-purple-300 transition-colors hover:border-purple-500"
>
	[about]
</a>
