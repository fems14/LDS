                max_context_chunk = round_down(max_context_chunk,
                                               self.block_size)
        self.chunked_prefill_for_mla = additional_config.get(
            "chunked_prefill_for_mla", False)
