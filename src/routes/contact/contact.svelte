
<script>
  export let link;
  export let name;
  export let svg;
</script>
				<div class="group relative mr-0">
					<a
						href={link}
						target="_blank"
						class=" text-purple-300 hover:text-purple-200"
						title={name}
					>
    {name}
								{@html svg}
						</a
					>
				</div>
