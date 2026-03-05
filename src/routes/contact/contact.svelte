
<script>
  let {contact} = $props();
</script>
				<div class="group relative mr-0">
					<a
						href={contact.link}
						target="_blank"
						class=" text-purple-300 hover:text-purple-200"
						title={contact.name}
					>
    {contact.name}
								{@html contact.svg}
						</a
					>
				</div>
