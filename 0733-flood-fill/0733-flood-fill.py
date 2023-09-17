class Solution:
    def flood(self, image: List[List[int]], sr: int, sc: int, color: int, og: int):
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]): return;

        if og != image[sr][sc]: return;

        image[sr][sc] = color;

        self.flood(image, sr-1, sc, color, og);
        self.flood(image, sr+1, sc, color, og);
        self.flood(image, sr, sc-1, color, og);
        self.flood(image, sr, sc+1, color, og);

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color: return image;
        self.flood(image, sr, sc, color, image[sr][sc]);
        return image;
    
