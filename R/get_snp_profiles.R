#' Extract SNP Profiles and Nucleotide Frequencies
#'
#' This function identifies polymorphic sites (SNPs) in a FASTA alignment
#' and returns a frequency table of nucleotides for each specific position.
#'
#' @param alignment_path Character; the path to the FASTA file (e.g., "Alignment.fasta").
#'
#' @return A matrix where rows are the actual SNP positions in the alignment
#'         and columns represent the frequencies of bases (a, c, g, t, -, etc.).
#' @importFrom ape read.dna seg.sites base.freq
#' @export

get_snp_profiles <- function(alignment_path) {
  
  if (!file.exists(alignment_path)) {
    stop("Error: The file does not exist at the specified path.")
  }
  
  dna <- ape::read.dna(alignment_path, format = "fasta")
  
  snp_indices <- ape::seg.sites(dna)
  
  if (is.null(snp_indices) || length(snp_indices) == 0) {
    message("Info: No SNP positions found in this alignment.")
    return(NULL)
  }

  dna_snp_subset <- dna[, snp_indices]
  
  snp_frequencies <- apply(dna_snp_subset, 2, function(x) {
    tmp_mat <- matrix(x, ncol = 1)
    class(tmp_mat) <- "DNAbin"
    return(ape::base.freq(tmp_mat, all = TRUE))
  })
  
  final_table <- t(snp_frequencies)
  
  rownames(final_table) <- snp_indices
  
  message(paste("Successfully processed", length(snp_indices), "SNP positions."))
  
  return(final_table)
}
